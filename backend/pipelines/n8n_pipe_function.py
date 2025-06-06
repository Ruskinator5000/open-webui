"""
title: Minimal Test Pipe
author: Ruskinator Test
version: 0.1.0
type: pipe
"""
from pydantic import BaseModel

class Pipe:
    class Valves(BaseModel):
        test_valve: str = "default_value"

    def __init__(self):
        self.id = "minimal_test_pipe_id" # Unique ID
        self.name = "Minimal Test Pipe - Display Name" # What you'll see in UI
        self.valves = self.Valves()
        print(f"[{self.id}] Minimal pipe initialized successfully!") # Log initialization

    async def pipe(self, body: dict, __user__=None, __event_emitter__=None, __event_call__=None) -> dict:
        print(f"[{self.id}] Minimal pipe's pipe() method CALLED with body: {body}") # Log when called
        
        messages = body.get("messages", [])
        if not messages: # Ensure there's a message list to append to
            body["messages"] = []
        
        body["messages"].append({"role": "assistant", "content": "Minimal pipe test successful!"})
        
        print(f"[{self.id}] Minimal pipe's pipe() method RETURNING body: {body}") # Log what's returned
        return body