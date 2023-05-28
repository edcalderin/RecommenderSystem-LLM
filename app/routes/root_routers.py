from fastapi import APIRouter
from fastapi.responses import HTMLResponse

root_router = APIRouter()


@root_router.get("/", summary="Welcome endpoint")
def root():
    return HTMLResponse(
        """
        <html>
            <body>
                <h1>Welcome to my recommender system using LLM</h1>
                    div>For getting start go to <a href=/docs>here</a></div>
            </body>
        </html>
        """
    )
