# src/cli/handlers.py

from core.api import APIClient
from core.orchestration import (
    SandboxOrchestrator,
    QuickScanOrchestrator,
    SearchOrchestrator
)
from core.classifier import TargetType

client = APIClient()
SandboxOrc = SandboxOrchestrator(client)
QuickScanOrc = QuickScanOrchestrator(client)
SearchOrc = SearchOrchestrator(client)


def handle_command(args):
    if args.command == "submit":
        handle_submit(args)
    elif args.command == "scan":
        handle_scan(args)
    elif args.command == "search":
        handle_search(args)
    else:
        raise RuntimeError("Unknown command")


def handle_submit(args):
    if args.file:
        result = SandboxOrc.run_file(args.file, args.env_id)
        print(result)

    elif args.url:
        result = SandboxOrc.run_url(args.url, args.env_id)
        print(result)


def handle_scan(args):
    if args.file:
        result = QuickScanOrc.run_file(args.file, args.scan_type)
        print(result)

    elif args.url:
        result = QuickScanOrc.run_url(args.url, args.scan_type)
        print(result)


def handle_search(args):
    if args.filename:
        result = SearchOrc.run_search(
            target=args.filename,
            target_type=TargetType.FILENAME
        )
    elif args.hash:
        result = SearchOrc.run_search(
            target=args.hash,
            target_type=TargetType.HASH
        )

    elif args.url:
        result = SearchOrc.run_search(
            target=args.url,
            target_type=TargetType.URL
        )

    elif args.domain:
        result = SearchOrc.run_search(
            target=args.domain,
            target_type=TargetType.DOMAIN
        )

    elif args.host:
        result = SearchOrc.run_search(
            target=args.host,
            target_type=TargetType.HOST
        )

    else:
        raise RuntimeError("No valid search argument provided")

    print(result)
