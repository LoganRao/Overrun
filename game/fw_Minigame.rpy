# ─────────────────────────────────────────
#  FLESH WALKER MINIGAME — minigame.rpy
# ─────────────────────────────────────────

# init python:
#     import random

#     # ── Difficulty state ──────────────────
#     fw_distance       = 0      # how far the player has walked
#     fw_lights_on      = True   # current light state
#     fw_health         = 3      # player lives / sanity
#     fw_active         = False  # is the minigame running?

#     # ── Escalation helpers ────────────────
#     def fw_dark_interval():
#         """Seconds between lights-out events. Shrinks with distance."""
#         return max(4.0, 14.0 - fw_distance * 0.5)

#     def fw_dark_duration():
#         """How long lights stay out. Grows with distance."""
#         return min(12.0, 3.0 + fw_distance * 0.6)

#     def fw_reaction_window():
#         """Seconds the player has to fire. Shrinks with distance."""
#         return max(1.2, 3.5 - fw_distance * 0.15)

#     # ── Audio pool ────────────────────────
#     # Add your audio files here.
#     # Each entry is (audio_file, correct_action_hint)
#     FW_QUESTIONS = [
#         ("audio/fw_q1.ogg", "shoot"),
#         ("audio/fw_q2.ogg", "shoot"),
#         ("audio/fw_q3.ogg", "shoot"),
#     ]