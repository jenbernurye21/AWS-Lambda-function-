import boto3
import logging
from datetime import datetime, timedelta, timezone
from botocore.exceptions import ClientError, BotoCoreError

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create EC2 client
ec2 = boto3.client("ec2")

# Retention period
RETENTION_DAYS = 365


def lambda_handler(event, context):
    """
    Deletes EC2 snapshots older than RETENTION_DAYS.
    """

    cutoff_date = datetime.now(timezone.utc) - timedelta(days=RETENTION_DAYS)
    deleted_count = 0
    failed_count = 0

    logger.info(f"Snapshot cleanup started. Cutoff date: {cutoff_date.isoformat()}")

    try:
        paginator = ec2.get_paginator("describe_snapshots")
        pages = paginator.paginate(OwnerIds=["self"])

        for page in pages:
            for snapshot in page.get("Snapshots", []):
                snapshot_id = snapshot["SnapshotId"]
                start_time = snapshot["StartTime"]

                if start_time < cutoff_date:
                    logger.info(f"Deleting snapshot: {snapshot_id}")

                    try:
                        ec2.delete_snapshot(SnapshotId=snapshot_id)
                        deleted_count += 1
                    except ClientError as e:
                        failed_count += 1
                        logger.error(
                            f"Failed to delete snapshot {snapshot_id}: {e.response['Error']['Message']}"
                        )

    except (ClientError, BotoCoreError) as e:
        logger.error(f"Failed to retrieve snapshots: {str(e)}")
        raise

    logger.info(
        f"Snapshot cleanup completed. "
        f"Deleted: {deleted_count}, Failed: {failed_count}"
    )

    return {
        "status": "completed",
        "deleted_snapshots": deleted_count,
        "failed_deletions": failed_count
    }
