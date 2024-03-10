# type: ignore[a,abbr,address,area,article,aside,audio,b,base,bdi,bdo,blockquote,body,br,button,canvas,caption,cite,code,col,colgroup,command,datalist,dd,del,details,dfn,div,dl,dt,em,embed,fieldset,figcaption,figure,footer,form,h1,h2,h3,h4,h5,h6,head,header,hgroup,hr,html,i,iframe,img,input,ins,kbd,keygen,label,legend,li,link,map,mark,math,menu,meta,meter,nav,noscript,object,ol,optgroup,option,output,p,param,pre,progress,q,rp,rt,ruby,s,samp,script,section,select,small,source,span,strong,style,sub,summary,sup,svg,table,tbody,td,textarea,tfoot,th,thead,time,title,tr,track,u,ul,var,video,wbr]
from sapphirecms import html
from pages import theme, navigation

html.initialize(__name__)

class Index(Page):
    def __init__(self):
        self.tree = theme.base(
            pagetitle="Sapphire Landing",
            content=[
                h1(children="Welcome to SapphireCMS"),
                p(children="SapphireCMS is a modern, open-source, and easy-to-use Content Management System (CMS) for building websites."),
                p(children="SapphireCMS is built on top of Python and is designed to be simple, flexible, and extensible. It is a great choice for building websites, blogs, and web applications. SapphireCMS is designed with simplicity, customizability, performance, and developer-friendliness in mind."),
                p(children="SapphireCMS features a powerful and flexible theming system, a pythonic templating engine, and a simple and easy-to-use API for building web applications."),
                p(children=["Read the documentation to get started with SapphireCMS."]),
            ],
            navigation=navigation,
        )