# src/cli/parser.py

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="hybrit",
        description="Hybrid Analysis CLI Tool"
    )

    parser.add_argument(
        "--api-key",
        required=True,
        help="Hybrid Analysis API key"
    )

    # ---------- mode selection ----------
    mode_group = parser.add_mutually_exclusive_group(required=True)

    mode_group.add_argument(
        "--submit",
        action="store_true",
        help="Sandbox submission"
    )

    mode_group.add_argument(
        "--scan",
        action="store_true",
        help="Quick scan"
    )

    mode_group.add_argument(
        "--search",
        action="store_true",
        help="Search HA database"
    )

    # ---------- common target args ----------
    target_group = parser.add_mutually_exclusive_group()

    target_group.add_argument(
        "--file",
        type=str,
        help="File path"
    )

    target_group.add_argument(
        "--url",
        type=str,
        help="URL"
    )

    # ---------- submit args ----------
    parser.add_argument(
        "--env-id",
        type=int,
        default=140,
        help="Sandbox environment id (default: 140)"
    )

    # ---------- scan args ----------
    parser.add_argument(
        "--scan-type",
        type=str,
        default="all",
        help="Quick scan type (default: all)"
    )

    # ---------- search args ----------
    search_group = parser.add_mutually_exclusive_group()

    search_group.add_argument(
        "--filename",
        type=str,
        help="Search by filename"
    )

    search_group.add_argument(
        "--hash",
        type=str,
        help="Search by hash"
    )

    search_group.add_argument(
        "--domain",
        type=str,
        help="Search by domain"
    )

    search_group.add_argument(
        "--host",
        type=str,
        help="Search by IP/host"
    )

    return parser
