---
title: AI Customer Support Simulator
emoji: 🎧
colorFrom: blue
colorTo: green
sdk: docker
app_port: 8000
tags:
  - openenv
---

# 🤖 AI Customer Support Simulator (OpenEnv)

This environment is a **real-world simulation** designed for the Meta AI Hackathon. It evaluates an agent's ability to handle complex customer service scenarios with empathy and accuracy.

## 🌟 Environment Overview
The simulator places an AI agent in a support role where it must resolve multi-turn customer issues. It uses a **deterministic grader** that scores responses based on professionalism and task-specific resolutions.

### 🎯 Tasks & Difficulty
1. **Easy Refund** (ID: 0): A simple request where the agent must validate the refund.
2. **Medium Frustration** (ID: 1): An upset customer requiring high empathy and de-escalation.
3. **Hard Escalation** (ID: 2): A complex case that requires a formal manager hand-off.

## 📊 Technical Specs
- **Observation Space**: 
  - `conversation`: History of the chat.
  - `step_count`: Number of turns taken.
  - `current_customer_query`: The specific text the agent needs to address.
- **Action Space**: 
  - `response`: A string containing the agent's reply.
- **Reward**: A float between `0.0` and `1.0` reflecting the quality of the response.

## 🚀 Local Setup & Testing
1. **Build Container**:
   ```bash
   docker build -t support-env .
