# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import logging

from fastapi import APIRouter  # type: ignore
from fastapi import Header  # type: ignore
from fastapi import Depends  # type: ignore

from typing import List

from wazo_applicationd.config import Config
from wazo_applicationd.discovery import Discovery
from wazo_applicationd.context import Context
from wazo_applicationd.service import Service
from wazo_applicationd import helpers

from wazo_applicationd.models.application import Application
from wazo_applicationd.models.node import Node

from .helpers import get_config
from .helpers import get_discovery
from .helpers import get_service

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/applications/{application_name}", response_model=Application)
async def register_application(
    application_name: str, discovery: Discovery = Depends(get_discovery)
) -> Application:
    return await discovery.register_application(application_name)


@router.put("/applications/{application_uuid}/calls/{call_id}/answer")
async def call_answer(
    application_uuid: str,
    call_id: str,
    config: Config = Depends(get_config),
    service: Service = Depends(get_service),
) -> None:
    context = await Context.from_resource_id(config, call_id)
    await service.channel_answer(context, call_id)


@router.post("/applications/{application_uuid}/nodes/{node_name}", response_model=Node)
async def create_node_with_calls(
    application_uuid: str,
    node_name: str,
    call_ids: List[str],
    config: Config = Depends(get_config),
    service: Service = Depends(get_service),
) -> Node:
    bridge_id = helpers.resource_uuid(application_uuid, node_name)
    await service.create_bridge_with_channels(bridge_id, call_ids)
    return Node(uuid=bridge_id)


@router.post("/applications/{application_uuid}/calls/{call_id}/mute/start")
async def mute_call(
    application_uuid: str,
    call_id: str,
    config: Config = Depends(get_config),
    service: Service = Depends(get_service),
):
    pass


@router.post("/applications/{application_uuid}/calls/{call_id}/mute/stop")
async def mute_call(
    application_uuid: str,
    call_id: str,
    config: Config = Depends(get_config),
    service: Service = Depends(get_service),
):
    pass


@router.delete("/applications/{application_uuid}/calls/{call_id}")
async def call_hangup(
    application_uuid: str,
    call_id: str,
    x_context_token: str = Header(None),
    config: Config = Depends(get_config),
    service: Service = Depends(get_service),
) -> None:
    pass

