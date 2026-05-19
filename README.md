# AI Chatbot Prototype

An Object-Oriented, low-latency AI chatbot designed as an "Optimistic Gaming Companion." Built in Python using the OpenAI API, this prototype provides encouraging, context-aware feedback to players using specific gaming terminology, optimized for fast-paced environments.

## Technical Features

* **Low-Latency Inference:** Utilizes `gpt-4o-mini` to prioritize the rapid response times critical for maintaining an uninterrupted competitive gaming experience.
* **Sliding Context Window:** Implements strict memory management. The architecture retains the core persona (System Prompt) and the four most recent conversational exchanges, preventing context window bloat, saving token costs, and reducing latency.
* **Rapid Persona Engineering:** The bot's personality is injected via a System Prompt, allowing for instant behavioral iteration without the need for time-intensive local model fine-tuning.
* **Graceful Degradation:** The script securely checks the OS environment for API keys. If an environment variable is missing, it elegantly falls back to prompting the user for manual entry via the terminal rather than crashing.

## Prerequisites

* Python 3.8 or higher
* An active [OpenAI API Key](https://platform.openai.com/api-keys)

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/NickyCKC/Personable-AI-Chabot-using-LLM.git](https://github.com/NickyCKC/Personable-AI-Chabot-using-LLM.git)
   cd Personable-AI-Chabot-using-LLM
   ```

3. **Install the required dependencies:**
   ```bash
   pip install openai
   ```

3. **Configure your API Key:**
For security, this application reads your OpenAI API key from your system's environment variables.

* **Windows (PowerShell):**
   ```PowerShell
   $env:OPENAI_API_KEY="your-api-key-here"
   ```
(Note: If the environment variable is not set, the script will prompt you to paste the key directly into the terminal upon execution).

**Usage**
Run the prototype directly from your terminal:

```bash
python chatbot.py
```
Type your prompt when "Player:" appears. To exit the companion, type "quit".

**Future Scalability: Multimodal Edge Integration**
While this iteration serves as a text-based LLM interface, the architecture is designed for modular expansion into real-time gaming applications. Future development roadmaps include:

* **Computer Vision Integration:** Utilizing OpenCV and Gaussian filtering on live gameplay video feeds to identify on-screen state changes (e.g., depleting health bars or minimap alerts).

* **Active Coaching:** Feeding processed edge-detection data directly into the LLM's context window, transforming the application from a reactive text bot into an active, multimodal in-game coach.
