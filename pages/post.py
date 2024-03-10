# type: ignore[a,abbr,address,area,article,aside,audio,b,base,bdi,bdo,blockquote,body,br,button,canvas,caption,cite,code,col,colgroup,command,datalist,dd,del,details,dfn,div,dl,dt,em,embed,fieldset,figcaption,figure,footer,form,h1,h2,h3,h4,h5,h6,head,header,hgroup,hr,html,i,iframe,img,input,ins,kbd,keygen,label,legend,li,link,map,mark,math,menu,meta,meter,nav,noscript,object,ol,optgroup,option,output,p,param,pre,progress,q,rp,rt,ruby,s,samp,script,section,select,small,source,span,strong,style,sub,summary,sup,svg,table,tbody,td,textarea,tfoot,th,thead,time,title,tr,track,u,ul,var,video,wbr]
from sapphirecms import html
from sapphirecms.storage import DATABASE
from pages import theme, navigation
import datetime

html.initialize(__name__)

class Post(Page):
    def __init__(self, slug):
        post = DATABASE.Post.get_by_slug(slug)
        self.tree = theme.base(
            pagetitle=post.title,
            content=[
                theme.post(
                    title=post.title,
                    content=post.content,
                    author=DATABASE.resolve_relation(post.author),
                    date=post.created_at,
                    comments=DATABASE.resolve_relation(post.comments),
                    likes=DATABASE.resolve_relation(post.likes)
                )
            ],
            navigation=navigation,
        )