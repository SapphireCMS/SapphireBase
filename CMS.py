from sapphirecms.networking import Server, Socket
from sapphirecms.routing import Router
from themes import get_active_theme

from pages.index import Index
from pages.docs import Docs

import config

router = Router()
server = Server(5, router, auto_reload=True, debug=True, secret_key=config.active.secret_key)

index = Index()
docs = Docs()

router.add_route("/", "GET")(lambda request: index.render())
router.add_route("/docs", "GET")(lambda request: docs.render())

router.add_subrouter(get_active_theme().Theme.router)

server.start([Socket("0.0.0.0", 80, 1024)])