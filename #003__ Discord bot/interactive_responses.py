import asyncio
from discord import Message

# Dictionary to keep track of timers and their states
# Structure: {channel_id: (task, end_time, is_paused, remaining_seconds)}
active_timers = {}

async def send_timer_completion_message(channel):
    await channel.send("Time to take a break!")

async def timer_task(duration, channel):
    await asyncio.sleep(duration)
    await send_timer_completion_message(channel)

async def start_timer(message: Message, duration=1800):  # 1800 seconds = 30 minutes
    channel_id = str(message.channel.id)
    if channel_id in active_timers:
        await message.channel.send("A timer is already running.")
        return

    # Start the timer task
    task = asyncio.create_task(timer_task(duration, message.channel))
    active_timers[channel_id] = (task, asyncio.get_event_loop().time() + duration, False, duration)
    await message.channel.send(f"Started a 30-minute Pomodoro timer.")

async def pause_timer(message: Message):
    channel_id = str(message.channel.id)
    if channel_id not in active_timers:
        await message.channel.send("No active timer to pause.")
        return

    task, end_time, is_paused, remaining = active_timers[channel_id]
    if is_paused:
        await message.channel.send("Timer is already paused.")
        return

    task.cancel()  # Cancel the current task
    remaining_minutes = max(0, end_time - asyncio.get_event_loop().time())/60 # Convert to minutes
    active_timers[channel_id] = (None, end_time, True, remaining_minutes)
    await message.channel.send(f"Paused the timer with {remaining_minutes} seconds remaining.")

async def resume_timer(message: Message):
    channel_id = str(message.channel.id)
    if channel_id not in active_timers:
        await message.channel.send("No paused timer to resume.")
        return

    _, _, is_paused, remaining = active_timers[channel_id]
    if not is_paused:
        await message.channel.send("Timer is not paused.")
        return

    task = asyncio.create_task(timer_task(remaining, message.channel))
    active_timers[channel_id] = (task, asyncio.get_event_loop().time() + remaining, False, remaining)
    await message.channel.send("Resumed the timer.")

async def cancel_timer(message: Message):
    channel_id = str(message.channel.id)
    if channel_id not in active_timers:
        await message.channel.send("No active timer to cancel.")
        return

    task, _, _, _ = active_timers.pop(channel_id)
    if task:
        task.cancel()
    await message.channel.send("Cancelled the timer.")
