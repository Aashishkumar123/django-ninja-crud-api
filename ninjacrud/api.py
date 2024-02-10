from ninja import NinjaAPI, Swagger

api = NinjaAPI(docs=Swagger())
api.add_router("/students/", "main.api.router")


@api.get("/")
def check_health(request):
    return {"status_code": "200", "message": "ok"}
