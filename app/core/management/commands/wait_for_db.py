"""
Django command to wait for database to be available.
"""
import time

from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self, *args, **options):
        """Entrypoint for command"""
        # Showing 'waiting' message to console
        self.stdout.write('Waiting for database...')
        # Defining boolean variable to store database status
        db_up = False
        # Looping while database is unavailable
        while db_up is False:
            try:
                # Setting db_up to true if database is available
                self.check(databases=['default'])
                db_up = True
            # Catching errors produced if db is still unavailable
            except (Psycopg2Error, OperationalError):
                # Showing 'waiting' message to console
                self.stdout.write('Database unavailable, waiting 1 second...')
                # Delaying next iteration by 1 second
                time.sleep(1)

        # Showing 'Success' message to console
        self.stdout.write(self.style.SUCCESS('Database available!'))
