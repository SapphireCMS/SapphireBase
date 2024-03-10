# Type: Theme
# type: ignore[a,abbr,address,area,article,aside,audio,b,base,bdi,bdo,blockquote,body,br,button,canvas,caption,cite,code,col,colgroup,command,datalist,dd,del,details,dfn,div,dl,dt,em,embed,fieldset,figcaption,figure,footer,form,h1,h2,h3,h4,h5,h6,head,header,hgroup,hr,html,i,iframe,img,input,ins,kbd,keygen,label,legend,li,link,map,mark,math,menu,meta,meter,nav,noscript,object,ol,optgroup,option,output,p,param,pre,progress,q,rp,rt,ruby,s,samp,script,section,select,small,source,span,strong,style,sub,summary,sup,svg,table,tbody,td,textarea,tfoot,th,thead,time,title,tr,track,u,ul,var,video,wbr]
from sapphirecms.routing import Router
from sapphirecms import html
from themes import Theme

html.initialize(__name__)

class THEME(Theme):
    name = "Sapphire"
    description = "This is the Sapphire theme."
    keywords = "theme"
    logo = "https://via.placeholder.com/256"
    favicon = "https://via.placeholder.com/32"
    author = "Author"
    author_email = "mail@sushantshah.dev"
    author_website = "https://www.sushantshah.dev"
    author_website_name = "Sushant Shah"
    license = "MIT"
    license_url = "https://opensource.org/licenses/MIT"
    version = "0.0.0"
    router = Router(f"Theme<{name}>", prefix=f"/theme/{name}", ctx=__name__, static_dir="assets", static_prefix="/assets")
    
    @router.add_route("/", methods=["GET"])
    @staticmethod
    def index(request):
        return Theme.base(h1(children=["Hello, World!"]), "Sapphire Landing").render()
    
    def navigation(self, items):
        return nav(children=[
            span(id="nav-brand", children=[
                a(href="/", children="Sapphire")
            ]),
            ul(id="nav-links", children=[
                li(children=[
                    a(href=url, children=name)
                ]) for name, url in items
            ])
        ])
    
    def footer(self, left=None, middle=None, right=None):
        return footer(children=[
            section(id="columns", children=[
                div(id="column-left", classes="column", children=[left]) if left else "",
                div(id="column-middle", classes="column", children=[middle]) if middle else "",
                div(id="column-right", classes="column", children=[right]) if right else ""
            ]),
            span(id="theme-info", children=[
                "Powered by",
                a(href="https://sapphirecms.dev", children="SapphireCMS"),
            ])
        ])
        
    def comment(self, comment):
        from sapphirecms.storage import DATABASE
        author = DATABASE.resolve_relation(comment.author)
        return div(children=[
            span(children=[
                img(src=author.profile_picture, alt=author.name, classes="avatar"),
                a(href="/user/"+author.username, children=author.name),
                " on ",
                comment.created_at.strftime("%d %B, %Y")
            ]),
            p(children=comment.content),
            div(children=[
                ul(children=[self.comment(reply) for reply in comment.replies]),
            ]) if len(comment.replies) > 0 else ""  
        ])
        
    def post(self, title, content, author, date, comments=[], likes=[], options={}):
        return article(children=[
            header(children=[
                h2(children=[title]),
                p(children=[
                    "By ",
                    a(href="/user/"+author.username, children=author.name),
                    " on ",
                    date.strftime("%d %B, %Y")
                ])
            ]),
            div(children=[span(children=elem) for elem in content], style="display: flex; flex-direction: column; align-items: flex-start; justify-content: center;"),
            div(children=[
                    h3(children=["Comments"]),
                    ul(children=[li(children=[self.comment(comment)]) for comment in comments])
                ] if len(comments) > 0 else ""
            )
        ])
        
    def toc(self, header, content):
        children = ul(children=[self.toc_element(k, v) for k, v in content.items()])
        return section(id="toc", children=[
            section(children=[h3(children=[header])] + children if type(children) == list else [h3(children=[header]), children], classes="sticky-top"),
            script(type="text/javascript", children="""
document.addEventListener("DOMContentLoaded", function() {
    let observer = new IntersectionObserver((entries, observer) => {
        entry = entries.find(entry => entry.isIntersecting);
        document.querySelectorAll(".toc-element a").forEach(link => {
            if ("href" in link.attributes) {
                link.parentElement.classList.remove("active");
            }
        });
        let name = entry.target.getAttribute("name");
        let link = document.querySelector(`.toc-element a[href="${name}"]`).parentElement;
        link.classList.add("active");
    }, {threshold: 0.5});
        
    document.querySelectorAll(".toc-element a").forEach(link => {
        if ("href" in link.attributes) {
            observer.observe(document.querySelector("a[name='"+link.getAttribute("href")+"']"));
        }
    });
});
            """)
        ])
        
    def toc_element(self, name, url, level=1):
        return li(classes=f"toc-element toc-level-{level}", children=[
            a(href=url, children=name) if isinstance(url, str) else [name, ul(children=[self.toc_element(k, v, level+1) for k, v in url.items()])]
        ])
    
    def base(self, content, pagetitle, description=None, keywords=None, **options):
        return html(lang="en", children=[
            head(children=[
                meta(charset="utf-8"),
                meta(name="viewport", content="width=device-width, initial-scale=1"),
                meta(name="description", content=description if description else self.config.description),
                meta(name="keywords", content=", ".join(keywords if keywords else self.config.keywords)),
                meta(name="author", content=self.config.author),
                title(children=[pagetitle]),
                link(rel="icon", href=self.config.favicon),
                link(rel="stylesheet", href="/theme/Sapphire/assets/css/base.css", defer="true"),
                link(rel="preconnect", href="https://fonts.googleapis.com/"),
                link(rel="preconnect", href="https://fonts.gstatic.com/", crossorigin=""),
                link(href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap", rel="stylesheet", defer="true"),
            ]+options.get("head", [])),
            body(children=[
                options.get("navigation", self.navigation([("Home", "/"), ("About", "/about"), ("Contact", "/contact")])) if options.get("show-navigation", True) else "",
                div(id="body", children=[
                    options.get("left_sidebar", self.toc("Table of Contents", {})) if options.get("show_left_sidebar", False) else "",
                    section(id="content", children=[
                        content
                    ]),
                    options.get("right_sidebar", self.toc("Table of Contents", {})) if options.get("show_right_sidebar", False) else "",
                ]),
                options.get("footer", self.footer(
                    left=div(children=[
                        p(children=[
                            "SapphireCMS is a CMS for developers, by developers. It is built on Python and is designed to be fast, secure, and easy to use."
                        ]),
                        p(children=[
                            "This is the landing page for SapphireCMS. To learn more, visit the ",
                            a(href="https://sapphirecms.dev", children="SapphireCMS website"),
                            "."
                        ])
                    ]),
                    middle=div(children=[
                        p(children=[
                            "SapphireCMS is a CMS for developers, by developers. It is built on Python and is designed to be fast, secure, and easy to use."
                        ]),
                        p(children=[
                            "This is the landing page for SapphireCMS. To learn more, visit the ",
                            a(href="https://sapphirecms.dev", children="SapphireCMS website"),
                            "."
                        ])
                    ]),
                    right=div(children=[
                        p(children=[
                            "SapphireCMS is a CMS for developers, by developers. It is built on Python and is designed to be fast, secure, and easy to use."
                        ]),
                        p(children=[
                            "This is the landing page for SapphireCMS. To learn more, visit the ",
                            a(href="https://sapphirecms.dev", children="SapphireCMS website"),
                            "."
                        ])
                    ])
                )) if options.get("show-footer", True) else ""
            ])
        ])
        
Theme = THEME()