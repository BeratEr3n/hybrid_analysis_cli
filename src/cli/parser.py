# src/cli/parser.py

import argparse

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="hybrit",
        description="Hybrid Analysis CLI Tool"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # ----------------- submit -----------------
    submit = subparsers.add_parser("submit", help="Sandbox submission")

    submit_group = submit.add_mutually_exclusive_group(required=True)
    submit_group.add_argument("--file", type=str, help="File path for sandbox")
    submit_group.add_argument("--url", type=str, help="URL for sandbox")

    submit.add_argument(
        "--env-id",
        type=int,
        default=140,
        help="Sandbox environment id"
    )

    # ----------------- scan (quick scan) -----------------
    scan = subparsers.add_parser("scan", help="Quick scan")

    scan_group = scan.add_mutually_exclusive_group(required=True)
    scan_group.add_argument("--file", type=str, help="File path for quick scan")
    scan_group.add_argument("--url", type=str, help="URL for quick scan")

    scan.add_argument(
        "--scan-type",
        type=str,
        default="all",
        help="Quick scan type (default: all)"
    )

    # ----------------- search -----------------
    search = subparsers.add_parser("search", help="Search HA database")

    search_group = search.add_mutually_exclusive_group(required=True)

    search_group.add_argument("--filename", type=str, help="Search by filename")
    search_group.add_argument("--target", type=str, help="Auto-detect target type (except filename)")

    search_group.add_argument("--hash", type=str, help="Search by hash")
    search_group.add_argument("--url", type=str, help="Search by URL")
    search_group.add_argument("--domain", type=str, help="Search by domain")
    search_group.add_argument("--host", type=str, help="Search by IP/host")

    return parser
