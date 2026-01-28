# FPS LOGIC

## Table of Contents

1. [Basics - Setup Phase](#basics---setup-phase)
2. [Core Truth](#core-truth)
3. [Why the Clock Exists](#why-the-clock-exists)
4. [What the Clock Object Stores](#what-the-clock-object-stores)
5. [What tick(fps) Really Does](#what-tickfps-really-does)
6. [Step-by-Step: Inside tick()](#step-by-step-inside-tick)
7. [Why tick() Affects Everything](#why-tick-affects-everything)
8. [Why Input Still Feels Responsive](#why-input-still-feels-responsive)
9. [Where tick() Must Be Called](#where-tick-must-be-called)
10. [Correct Mental Model](#correct-mental-model)
11. [Why Clock Is an Object](#why-clock-is-an-object)
12. [Small Experiment (Proof)](#small-experiment-proof)
13. [Final Summary](#final-summary)

---

## Basics - Setup Phase

The **setup phase** runs once at the start of your program. This is where you:

- Initialize pygame
- Create the window (surface)
- Load images
- Define colors
- Create the Clock
- Define FPS
- Set starting values

> **Important:** This happens **outside the game loop** since the loop runs repetitively. It wouldn't make sense to put memory allocation inside a loop since it will keep renewing memory.

We keep all constants and values that we need to save **outside the loop**. This allows the game loop to:
- Access these values (since they are in the global scope)
- Reassign these values according to what happens in the game

### Creating the Clock

In pygame, we use `pygame.time.Clock()` to manage time between frames. It's a constructor method that returns a Clock object containing methods to help us control FPS.

```python
fps_clock = pygame.time.Clock()

while True:
    fps_clock.tick(30)  # Limit to 30 frames per second
```

---

## Core Truth

> **The Clock object does NOT control your game loop.**  
> **Your game loop controls the Clock.**

The Clock is only:
- A container for time-related state
- A helper that can pause execution when needed

**Nothing more.**

---

## Why the Clock Exists

Computers run at different speeds. Without time control:

- Fast machines run the loop too fast
- Slow machines run it slower
- Movement, animation, and input become inconsistent

The Clock exists to **pace frames** consistently across all hardware.

---

## What the Clock Object Stores

Conceptually, a `pygame.time.Clock` instance stores values like:

```
last_tick_time
time_passed_since_last_frame
target_frame_time
```

**It does NOT:**
- Run code
- Trigger rendering
- Schedule frames
- Control your loop automatically

---

## What tick(fps) Really Does

Example call:

```python
clock.tick(30)
```

This does **not** mean 30 seconds.

It means:

```
target_frame_time = 1 second / 30 frames
                  ≈ 33.33 milliseconds per frame
```

---

## Step-by-Step: Inside tick()

### 1. Get the current system time

```python
now = current_system_time
```

### 2. Calculate how long the previous frame took

```python
frame_time = now - last_tick_time
```

This answers: *"How fast did the last loop iteration run?"*

### 3. Compare against the target frame time

```python
if frame_time < 33ms:
    sleep(33ms - frame_time)
```

**This is the entire mechanism.** The clock simply sleeps if the frame was too fast.

### 4. Update internal state

```python
last_tick_time = current_system_time
```

The clock is now ready for the next frame.

---

## That Is Literally It

- No scheduling
- No permissions
- No frame gating

Just:
- Time measurement
- Conditional sleeping
- Repeated every loop iteration

---

## Why tick() Affects Everything

Python is **single-threaded**.

When `tick()` sleeps:
- Input handling waits
- Game logic waits
- Rendering waits
- The loop pauses as a whole

**This is GOOD** — it keeps everything synchronized.

---

## Why Input Still Feels Responsive

Because:
- Sleep times are very small (milliseconds)
- Input is checked many times per second
- Humans cannot perceive ~16–33 ms delays

So responsiveness stays high.

---

## Where tick() Must Be Called

`tick()` must be called **once per frame**, inside the game loop.

### ✅ Correct Usage

```python
while running:
    clock.tick(30)
    handle_events()
    update_logic()
    draw()
```

### ❌ Incorrect Usage

| Mistake | Result |
|---------|--------|
| Calling it outside the loop | Useless |
| Calling it twice per loop | Double delay |
| Not calling it | Unlimited FPS and high CPU usage |

---

## Correct Mental Model

Your program behaves like this:

```
run loop → check time → maybe sleep → next loop → check time → maybe sleep
```

The Clock is only the **"maybe sleep" decision-maker**.

---

## Why Clock Is an Object

Because it must remember:
- When the last frame happened
- How much time passed between frames
- Average FPS (for debugging)

That memory must persist → **object**.

---

## Small Experiment (Proof)

Inside your game loop:

```python
print(clock.tick(30))
```

Typical output:

```
32
33
34
```

These numbers are the **actual frame durations in milliseconds**.

No magic. Just math + sleep + repetition.

---

## Final Summary

| Concept | Reality |
|---------|---------|
| Clock does not run your game | ✅ True |
| `tick()` does not allow frames | ✅ True |
| `tick()` only slows the loop if it is too fast | ✅ True |
| FPS control = time measurement + conditional sleeping | ✅ True |

**Once this clicks, pygame timing, movement, and animation all make sense.**
