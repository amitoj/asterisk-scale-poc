# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import asyncio
import logging
import consul.aio  # type: ignore
import uvicorn  # type: ignore
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

from typing import Any
from typing import Callable
from typing import Awaitable

from .config import Config
from .discovery import Discovery
from .service import Service
from .context import Context

from .routers import application
from .routers import status

logger = logging.getLogger(__name__)


class API:

    config: Config
    discovery: Discovery
    fastapi: FastAPI
    service: Service

    def __init__(self, config: Config, discovery: Discovery, service: Service):
        self.config = config
        self.discovery = discovery
        self.service = service

        self.app = FastAPI(
            title="Wazo applicationd",
            description="Applicationd blah blah",
            version="0.1.0",
        )

        self.setup_middlewares()
        self.setup_routes()

    def setup_routes(self) -> None:
        self.app.include_router(status.router, tags=["status"])
        self.app.include_router(application.router, prefix="/1.0", tags=["application"])

    def setup_middlewares(self) -> None:
        self.app.middleware("http")(self.inject_deps)

    async def inject_deps(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        response = Response("Internal server error", status_code=500)
        try:
            request.state.config = self.config
            request.state.discovery = self.discovery
            request.state.service = self.service

            response = await call_next(request)
        finally:
            pass
        return response

    async def run(self) -> None:
        logger.info("Start API")

        try:
            log_level = logging.INFO
            if self.config.get("debug"):
                log_level = logging.DEBUG

            config = uvicorn.Config(
                self.app,
                host="0.0.0.0",
                port=self.config.get("port"),
                log_level=log_level,
            )

            server = uvicorn.Server(config)

            await server.serve()
        except asyncio.CancelledError:
            pass