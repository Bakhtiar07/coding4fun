import asyncio
from discord import Message

# Dictionary to keep track of timers
# Structure: {channel_id: (task, end_time)}
active_timers = {}

async def start_or_resume_timer(message: Message, duration=None):
    # Assuming this function already properly starts or resumes a timer.
    pass

async def pause_timer(message: Message):
    channel_id = str(message.channel.id)
    if channel_id in active_timers:
        task, _ = active_timers[channel_id]
        task.cancel()  # Cancels the currently running timer task
        # Note: You might want to adjust this to actually pause instead of cancel, which would require more complex logic.
        await message.channel.send("Timer paused.")
    else:
        await message.channel.send("No active timer to pause.")

async def cancel_timer(message: Message):
    channel_id = str(message.channel.id)
    if channel_id in active_timers:
        task, _ = active_timers.pop(channel_id)  # Removes the timer from active_timers and cancels the task
        task.cancel()
        await message.channel.send("Timer canceled.")
    else:
        await message.channel.send("No active timer to cancel.")
