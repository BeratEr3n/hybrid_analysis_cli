# src/cli/handlers.py

from core.api import APIClient
from core.orchestration import (
    SandboxOrchestrator,
    QuickScanOrchestrator,
    SearchOrchestrator
)
from core.classifier import TargetType


def handle_command(args):
    client = APIClient(api_key=args.api_key)

    sandbox_orc = SandboxOrchestrator(client)
    quickscan_orc = QuickScanOrchestrator(client)
    search_orc = SearchOrchestrator(client)

    if args.submit:
        handle_submit(args, sandbox_orc)

    elif args.scan:
        handle_scan(args, quickscan_orc)

    elif args.search:
        handle_search(args, search_orc)

    else:
        raise RuntimeError("No mode selected")


def handle_submit(args, sandbox_orc):
    if args.file:
        result = sandbox_orc.run_file(args.file, args.env_id)

    elif args.url:
        result = sandbox_orc.run_url(args.url, args.env_id)

    else:
        raise RuntimeError("--submit requires --file or --url")

    print(result)


def handle_scan(args, quickscan_orc):
    if args.file:
        result = quickscan_orc.run_file(args.file, args.scan_type)

    elif args.url:
        result = quickscan_orc.run_url(args.url, args.scan_type)

    else:
        raise RuntimeError("--scan requires --file or --url")

    print(result)


def handle_search(args, search_orc):
    if args.filename:
        target = args.filename
        target_type = TargetType.FILENAME

    elif args.hash:
        target = args.hash
        target_type = TargetType.HASH

    elif args.url:
        target = args.url
        target_type = TargetType.URL

    elif args.domain:
        target = args.domain
        target_type = TargetType.DOMAIN

    elif args.host:
        target = args.host
        target_type = TargetType.HOST

    else:
        raise RuntimeError("No valid search argument provided")

    result = search_orc.run_search(
        target=target,
        target_type=target_type
    )

    print(result)
