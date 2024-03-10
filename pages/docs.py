# type: ignore[a,abbr,address,area,article,aside,audio,b,base,bdi,bdo,blockquote,body,br,button,canvas,caption,cite,code,col,colgroup,command,datalist,dd,del,details,dfn,div,dl,dt,em,embed,fieldset,figcaption,figure,footer,form,h1,h2,h3,h4,h5,h6,head,header,hgroup,hr,html,i,iframe,img,input,ins,kbd,keygen,label,legend,li,link,map,mark,math,menu,meta,meter,nav,noscript,object,ol,optgroup,option,output,p,param,pre,progress,q,rp,rt,ruby,s,samp,script,section,select,small,source,span,strong,style,sub,summary,sup,svg,table,tbody,td,textarea,tfoot,th,thead,time,title,tr,track,u,ul,var,video,wbr]
from sapphirecms import html
from pages import theme, navigation
import pygments

html.initialize(__name__)

class Docs(Page):
    sections = {
        "introduction": ("Introduction", [
            p(children="SapphireCMS is a modern, open-source, and easy-to-use Content Management System (CMS) for building websites. It is built on top of Python and is designed to be simple, flexible, and extensible. It is a great choice for building websites, blogs, and web applications. SapphireCMS is designed with simplicity, customizability, performance, and developer-friendliness in mind."),
        ]),
        "installation": ("Installation", {
            "prerequisites": ("Prerequisites", [
                ul(children=[
                    li(children="Python 3.10 or higher"),
                    li(children="A supported database (currentgly: MongoDB)"),
                    li(children="A web server (optional)"),
                ]),
            ]),
            "installation": ("Installation", [
                ol(children=[
                    li(children=[
                        "Get the latest version of SapphireCMS from the official git repository.",
                        code_block("git clone https://github.com/sapphire-cms/sapphirecms.git", language="bash")
                    ]),
                    li(children=[
                        "Install the required dependencies.",
                        code_block("$~ cd sapphirecms\n$~ python3 -m pip install -r requirements.txt", language="bash")
                    ]),
                    li(children="Modify configuration and general settings in the config.py file. Don't forget to set the secret key and database credentials."),
                    li(children=[
                    "Run the server.",
                        code_block("$~ python3 -m CMS", language="bash")
                    ]),
                    li(children="Make your site public:"),
                    ul(children=[
                        li(children="You have a server with a static public IP address and a domain name."),
                        ol(children=[
                            li(children="Set up a reverse proxy (e.g. Nginx or Apache)"),
                            li(children="Set up a firewall (e.g. UFW)"),
                            li(children="Set up SSL/TLS (e.g. Let's Encrypt)"),
                        ]),
                        li(children="You have a server with a dynamic public IP address and a domain name."),
                        ol(children=[
                            li(children="Set up a cloudflared tunnel"),
                            li(children="Set up a firewall (e.g. UFW)"),
                            li(children="Set up SSL/TLS (e.g. Cloudflare)"),
                        ]),
                    ]),
                ]),
            ]),
            "configuration": ("Configuration", [
                p(children="The documentation for SapphireCMS is coming soon."),
            ]),
        }),
        "theming": ("Theming", [
            p(children="The documentation for SapphireCMS is coming soon."),
        ]),
    }
    
    def __init__(self):
        self.tree = theme.base(
            pagetitle="SapphireCMS Documentation",
            head=[
                style(children=pygments.formatters.HtmlFormatter().get_style_defs(".code-block"))
            ],
            content=[
                h1(children="SapphireCMS Documentation"),
                p(children="The documentation for SapphireCMS."),
                self.generate_docs(),
            ],
            navigation=navigation,
            left_sidebar=theme.toc(
                header="Documentation",
                content={
                    "Introduction": "#introduction",
                    "Installation": {
                        "Prerequisites": "#prerequisites",
                        "Installation": "#installation",
                        "Configuration": "#configuration"
                    },
                    "Theming": "#theming",
                },
            ),
            show_left_sidebar=True,
        ).prerendered()

    def generate_docs(self, sections=sections, level=0):
        content = section()
        levels = [h2, h3, h4, h5, h6]
        for key, value in sections.items():
            if isinstance(value[1], list):
                content += div(
                    id=key,
                    children=[
                        a(name=f"#{key}", children=levels[level](children=value[0])),
                        section(children=value[1]),
                    ],
                )
            elif isinstance(value[1], dict):
                content += div(
                    id=key,
                    children=[
                        a(name=f"#{key}", children=levels[level](children=value[0])),
                        self.generate_docs(value[1], level+1),
                    ],
                )
        return content