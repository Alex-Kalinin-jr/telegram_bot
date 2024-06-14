import ngrok
from fastapi import FastAPI, APIRouter
from config import BOT_TOKEN, NGROK_TOKEN
from bot import bot, dp
from routers.fastapi_router import router as fastapi_router


async def lifespan(app):
    tmp = await ngrok.forward(8000, authtoken=NGROK_TOKEN)
    forward_url = tmp.url()
    
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(url=f"{forward_url}/bot/{BOT_TOKEN}")

    yield

    await bot.session.close()

app = FastAPI(lifespan=lifespan)
app.include_router(fastapi_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
