# Automated Content Engine



# Automated Content Engine

**Automated Content Engine** is a fully automated pipeline for generating high-quality scripts and converting them into audio content for platforms like YouTube Shorts and Instagram Reels. Built for scalability and efficiency, this engine leverages modern AI tools to minimize manual work and maximize output quality.

---

## 🚀 Project Overview

The engine is designed to automate the **entire content creation workflow**:

1. **Text Script Generation**  
   - Uses **Ollama Mistral** to generate text scripts from predefined prompts (`prompts.json`).  
   - Each prompt can generate multiple variations of scripts.  
   - Scripts are saved in the `generated/` folder for easy access.

2. **Text-to-Speech Conversion**  
   - Uses **KittenTTS** to convert generated scripts into high-quality audio files.  
   - Audio outputs are stored in the `audio/` folder, ready for publishing.

3. **Automation & Scheduling (Future)**  
   - Integrates with **n8n** or cron jobs to run the pipeline fully autonomously.  
   - The system will be capable of generating and publishing content without manual intervention.

---

## 📁 Directory Structure

automated_content_engine/
│
├─ audio/ # Stores TTS audio files
├─ generated/ # Stores AI-generated text scripts
├─ generate_text.py # Generates scripts using Ollama Mistral
├─ kitten_tts.py # Converts scripts to audio using KittenTTS
├─ prompts.json # All predefined prompts for text generation
└─ README.md # Project overview and documentation

## ⚡ Technology Stack

- **Text Generation:** Ollama Mistral  
- **Text-to-Speech:** KittenTTS  
- **Automation:** n8n / cron jobs (planned)  
- **Programming Language:** Python


## 🔒 Security Best Practices

- **Secrets Management:** API keys are never hardcoded; stored in environment variables.  
- `.env` is added to `.gitignore` to ensure sensitive credentials are never pushed to GitHub.


## 🎯 Project Vision

- Fully autonomous content engine for **YouTube Shorts and Instagram Reels**.  
- Efficient script generation → high-quality audio conversion → ready-to-publish content.  
- Lightweight, maintainable, and built with **modern AI tools**. 


## 📌 Notes for Recruiters

This project demonstrates:

- **AI Integration Skills:** Using cutting-edge models for content automation.  
- **Backend Automation:** Full pipeline design with storage and workflow management.  
- **Security Awareness:** API keys and secrets handled correctly.  
- **Clean Code & Structure:** Well-organized directories and modular scripts.  

---

*Made by Mark Heaven
