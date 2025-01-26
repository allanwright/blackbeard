#!/usr/bin/env python3
import sys

def calculate_sleep_seconds(startup_time, shutdown_time):
    power_on_parts = startup_time.split(":")
    power_off_parts = shutdown_time.split(":")
    power_on_seconds = (int(power_on_parts[0]) * 3600) + (int(power_on_parts[1]) * 60)
    power_off_seconds = (int(power_off_parts[0]) * 3600) + (int(power_off_parts[1]) * 60)
    if power_on_seconds < power_off_seconds:
        sleep_seconds = (24 * 3600) - (power_off_seconds - power_on_seconds)
    else:
        sleep_seconds = power_on_seconds - power_off_seconds
    return sleep_seconds

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python calculate_sleep_seconds.py <startup_time> <shutdown_time>")
        sys.exit(1)

    startup_time = sys.argv[1]
    shutdown_time = sys.argv[2]

    sleep_seconds = calculate_sleep_seconds(startup_time, shutdown_time)
    print(sleep_seconds)