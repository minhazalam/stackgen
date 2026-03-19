# 🚀 Stackgen CLI

**Stackgen** is a developer-first CLI tool to **bootstrap production-ready data engineering projects** in seconds.

Build batch, streaming, or full data pipelines with a single command.

---

## ✨ Features

* ⚡ Generate complete data engineering project scaffolds
* 🧠 Supports **Batch, Streaming, and Full pipelines**
* 🐳 Built-in **Docker-based infrastructure setup**
* 🔄 Includes **Spark, Kafka, Airflow integrations**
* 🎯 Interactive CLI with clean UX
* 🧩 Template-based architecture (Jinja2)

---

## 🧱 Supported Pipelines

### 🟢 Batch Pipeline

* Apache Spark (batch jobs)
* Apache Airflow (orchestration)

### 🔴 Streaming Pipeline

* Apache Kafka (event streaming)
* Spark Structured Streaming

### 🔥 Full Pipeline

* Batch + Streaming combined

---

## ⚡ Install

```bash
pip install stackgen-cli
```

## 🚀 Quickstart

```bash
stackgen init my-project
```

---

### CLI Experience

```text
? Select pipeline type:
❯ Batch Pipeline (Spark + Airflow)
  Streaming Pipeline (Kafka + Spark)
  Full Pipeline (Spark + Airflow + Kafka)
```

---

### Run Generated Project

```bash
cd my-project
docker-compose up
```

---

## 📁 Example Generated Structure

```text
my-project/
├── airflow/           # DAGs
├── spark/jobs/        # Batch & streaming jobs
├── kafka/             # Kafka producer (if streaming)
├── config/            # Config files
├── docker-compose.yml
└── requirements.txt
```

---

## 🛠️ Tech Stack

* **Python**
* **Apache Spark**
* **Apache Kafka**
* **Apache Airflow**
* **Docker**
* **Jinja2 (templating)**

---

## 🧠 How It Works

1. CLI collects user input (pipeline type)
2. Generator builds project structure
3. Jinja templates render files dynamically
4. Docker setup enables instant execution

---

## 🛣️ Roadmap

* [ ] Feature toggles (Kafka / Airflow selection)
* [ ] Config-driven generation (YAML support)
* [ ] Cloud integrations (S3, Snowflake, BigQuery)
* [ ] Plugin system for custom stacks
* [ ] CI/CD pipeline templates

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit PRs.

---

## 📌 Vision

Stackgen aims to become a **go-to CLI tool for data engineers** to quickly bootstrap scalable and production-ready data platforms.

---

## 👨‍💻 Author

Minhaz Alam

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
