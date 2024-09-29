# main.py

import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from utils.logger_config import get_logger

# Load environment variables
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Initialize the logger
logger = get_logger(__name__)

# Initialize Supabase client with error handling
try:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    logger.info("Supabase client initialized successfully.")
except Exception as e:
    logger.critical(f"Failed to initialize Supabase client: {e}", exc_info=True)
    raise e  # Re-raise exception after logging

# Create FastAPI app instance
app = FastAPI()

# Log application startup
logger.info("Starting FastAPI application.")

# CORS settings
origins = [
    "https://lutools.luca137.com",  # Your frontend domain
    "http://localhost",              # Include localhost for testing
    "http://127.0.0.1",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware to log each request and response
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")
    try:
        response = await call_next(request)
        logger.info(f"Response status: {response.status_code}")
        return response
    except Exception as exc:
        logger.error(f"Error processing request: {exc}", exc_info=True)
        raise exc  # Re-raise the exception for global handlers

# Exception handler for uncaught exceptions
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.critical(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"},
    )

# Exception handler for HTTP exceptions
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    logger.warning(f"HTTP exception: {exc.detail}", exc_info=True)
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

# Exception handler for request validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.warning(f"Validation error: {exc.errors()}", exc_info=True)
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )

# Example endpoint with error handling
@app.get("/ping")
async def ping():
    logger.debug("Ping endpoint called.")
    try:
        # Simulate processing logic here
        return {"message": "pong"}
    except Exception as e:
        logger.error(f"Error in /ping endpoint: {e}", exc_info=True)
        raise e  # Let the global exception handler process it

# Additional endpoints can be added below
# Remember to include appropriate logging and error handling
