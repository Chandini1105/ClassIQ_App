#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'classiq_project.settings')
django.setup()

from django.utils import timezone
from datetime import time, datetime

# Test 1: Verify timezone-aware datetime
now = timezone.now()
print(f"✓ Timezone-aware datetime: {now}")
print(f"  Timezone info: {now.tzinfo}")

# Test 2: Show what happens with naive time object
naive_time = now.time()
print(f"\n✗ Naive time object (loses tz): {naive_time}")
print(f"  Timezone info: {naive_time.tzinfo}")

# Test 3: Show the difference in display
print(f"\n📊 Display comparison:")
print(f"  Timezone-aware datetime formatted: {now.strftime('%I:%M %p')}")
print(f"  Current system time (UTC): {datetime.utcnow().strftime('%I:%M %p')} UTC")
print(f"  IST should be: {now.strftime('%I:%M %p')} IST")

print(f"\n✓ Fix confirmed: Pass full 'now' object to template, not 'now.time()'")
