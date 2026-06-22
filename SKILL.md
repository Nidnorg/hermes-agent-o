# Hermes Claw Agent – Skill Definition

## Description
Agent combinant les capacités de Hermes et OpenClaw pour assistance conversationnelle, automatisation et contrôle multi-plateforme.  

---

## Capabilities

| Action       | Outils/OpenClaw        | Exemple d'utilisation |
|--------------|------------------------|-----------------------|
| Conversation | `model:optr-hermes-8x7b` | Prompts longs, contexte, reformulation |
| Shell        | `exec`                 | Lancer des scripts, modifier des fichiers |
| Navigateur   | `browser`              | Scraping, remplissage de formulaires |
| Fichiers     | `read/write/edit`      | Manipulation de fichiers locaux |
| TaskFlow     | `taskflow`             | Workflows asynchrones et rappel |
| Skills       | `skill_workshop`       | Proposer des compétences |
| Android      | `openclaw-android`     | Control apps, gestes, texte |
| Web Search   | `web_search` + `weather` | Infos temps réel, actualités |

---

## Quick-start

```json
{
  "agent": "hermes-claw",
  "prompt": "Planifie une réunion et envoie un rappel Slack."
}
```

---

## License
MIT