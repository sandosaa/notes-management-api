from fastapi import APIRouter

from src.api.v1.endpoints import notes

# --- TEACHING: THE ROUTER AGGREGATOR ---
# In a large-scale application, you will have many different modules
# (Notes, Users, AI, etc.). This 'api_router' acts as a central hub "hmm when did we hear this before" or
# "Master Switchboard" that collects all individual routers and bundles
# them together into a single object.
api_router = APIRouter()

# Zatuna: Routing and Prefixes
# By using 'include_router', we mount the notes endpoints onto our router.
# 1. 'prefix="/notes"': Every URL in the notes module will automatically
#    start with /notes (e.g., GET /api/v1/notes/).
# 2. 'tags=["notes"]': This groups these endpoints together in the Swagger UI,
#    making it much easier for other developers to navigate.
api_router.include_router(notes.router, prefix="/notes", tags=["notes"])
