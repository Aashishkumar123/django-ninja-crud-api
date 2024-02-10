from ninja import NinjaAPI, Swagger

api = NinjaAPI(docs=Swagger())
api.add_router("/students/", "main.api.router")
