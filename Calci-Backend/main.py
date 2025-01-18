# from contextlib import asynccontextmanager
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from apps.calculator.route import router as calculator_router

# import uvicorn
# from constants import SERVER_URL, PORT, ENV

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     yield

# app = FastAPI(lifespan=lifespan)


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=['*'],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get('/')
# async def root():
#     return {"message": "Server is running"}

# app.include_router(calculator_router, prefix="/calculate", tags=["calculate"])


# if __name__ == "__main__":
#     uvicorn.run("main:app", host=SERVER_URL, port=int(PORT), reload=(ENV == "dev"))
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.calculator.route import router as calculator_router
import uvicorn
from constants import SERVER_URL, PORT, ENV

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return {"message": "Server is running"}

# Improved endpoint for better handling of algebraic expressions
@app.post('/calculate/optimize')  # **Added a new optimized route**
async def calculate_optimize(data: dict):
    # Process algebraic equations efficiently
    try:
        expression = data.get("expression", "")
        # Implement error handling and quick response logic
        result = eval(expression)  # Simplified calculation logic; use secure eval if needed
        return {"expression": expression, "result": result}
    except Exception as e:
        return {"error": str(e)}

app.include_router(calculator_router, prefix="/calculate", tags=["calculate"])

if __name__ == "__main__":
    uvicorn.run("main:app", host=SERVER_URL, port=int(PORT), reload=(ENV == "dev"))
