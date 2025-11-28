# 第六阶段：AI应用生产部署与DevOps

在完成了AI全栈综合项目之后，学习如何将AI应用部署到生产环境至关重要。这一阶段将帮助你掌握AI应用特有的部署技术和实践，确保你的AI服务可以稳定、高效地运行在生产环境中。

## 学习内容

### 1. AI应用容器化 (重点加强)
- **Docker 基础概念和原理**
- **AI应用Dockerfile优化**:
  - 依赖预安装以减少镜像大小
  - 模型缓存策略
  - GPU支持配置 (如需要)
- **多阶段构建**: 优化AI应用镜像构建
- **Docker Compose 多服务编排**: 应用 + 数据库 + Redis + 向量数据库
- **容器安全最佳实践**
- **镜像版本管理和发布策略**

### 2. AI应用部署策略 (重点)
- **云平台选择 (AWS, GCP, Azure, 阿里云等)**:
  - 适合AI应用的云服务 (GPU实例、向量数据库服务)
  - 成本优化策略
- **环境隔离 (开发/测试/生产)**
- **CI/CD 流水线设置 (GitHub Actions, GitLab CI)**:
  - AI模型版本管理
  - 自动化测试 (功能测试 + AI响应质量测试)
- **零停机部署策略**: 对话历史保持、状态迁移
- **配置管理与环境变量**: API密钥、模型配置等

### 3. AI应用监控与日志 (Observability)
- **应用性能监控 (APM) - Prometheus + Grafana**:
  - AI响应时间监控
  - 向量查询性能监控
  - API调用频率监控
  - 成本监控 (API调用次数)
- **日志收集与分析**:
  - ELK Stack (Elasticsearch, Logstash, Kibana) 或 Loki
  - AI调用日志记录 (输入/输出追踪)
- **错误追踪**: Sentry 或类似工具
- **健康检查与告警**:
  - AI服务可用性监控
  - 向量数据库连接监控
- **AI性能指标**: 响应质量、准确性监控

### 4. AI应用性能优化 (重点)
- **Web服务器优化 (Nginx, Apache)**: 处理AI流式响应
- **反向代理配置**: 超时设置、连接管理
- **负载均衡策略**: 智能路由(考虑会话亲和性)
- **缓存策略**:
  - AI结果缓存 (降低API成本)
  - 向量搜索结果缓存
  - 嵌入缓存
- **数据库连接池优化**
- **AI服务扩展策略**: 水平扩展、模型服务集群

### 5. AI应用安全实践 (重点加强)
- **容器安全扫描**
- **依赖包漏洞扫描**
- **HTTPS/TLS 配置**
- **API 认证与授权 (JWT, OAuth2)**:
  - 用户认证
  - AI API密钥管理
- **网络安全 (防火墙、VPC)**
- **安全凭证管理**: HashiCorp Vault, AWS Secrets Manager
- **AI安全**: 提示注入防护、内容过滤

### 6. AI/RAG应用特殊考虑 (核心重点)
- **模型服务部署策略**:
  - vLLM (高性能模型推理)
  - TGI (文本生成推理)
  - Ollama (本地模型部署)
- **GPU资源管理**: 资源分配、成本控制
- **批处理与流处理优化**: 提高吞吐量
- **响应时间优化**: 降低AI延迟
- **模型版本管理**: 模型更新、回滚
- **成本监控和优化**: API调用成本、计算资源成本

## 容器化实践 (AI重点)

### AI应用Dockerfile示例
```dockerfile
# 多阶段构建 - 为AI应用优化
# 构建阶段
FROM python:3.11-slim as builder
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && \
    poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt

# 运行阶段 - 为AI应用优化
FROM python:3.11-slim
RUN useradd --create-home --shell /bin/bash app
WORKDIR /home/app
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*

# 预安装AI相关依赖
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

COPY --chown=app:app . .
USER app
EXPOSE 8000

# 为AI应用优化启动参数
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
```

### AI应用Docker Compose配置
```yaml
# docker-compose.yml - AI应用多服务
version: "3.8"
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/myapp
      - REDIS_URL=redis://redis:6379/0
      - VECTOR_DB_URL=postgresql://user:password@vector_db:5432/myapp
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    depends_on:
      - db
      - redis
      - vector_db
    volumes:
      - ./data:/app/data
    # 为AI应用调整资源限制
    deploy:
      resources:
        limits:
          memory: 2G
          cpus: '1.0'

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data

  vector_db:
    image: pgvector/pgvector:pg15
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - vector_data:/var/lib/postgresql/data

volumes:
  postgres_data:
  redis_data:
  vector_data:
```

## CI/CD 实践 (AI增强版)

### GitHub Actions - AI应用流水线
```yaml
# .github/workflows/ai-deploy.yml
name: AI App Deploy to Production

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.11'
    - name: Install dependencies
      run: |
        pip install poetry
        poetry install
    - name: Run tests
      run: |
        poetry run pytest
    - name: Run AI response quality tests
      run: |
        poetry run pytest tests/ai_tests.py
    - name: Run linting
      run: |
        poetry run ruff check .
        poetry run mypy .

  build-and-push:
    needs: test
    runs-on: ubuntu-latest
    steps:
    - name: Checkout
      uses: actions/checkout@v3
    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v2
    - name: Login to DockerHub
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKERHUB_USERNAME }}
        password: ${{ secrets.DOCKERHUB_TOKEN }}
    - name: Build and push
      uses: docker/build-push-action@v4
      with:
        context: .
        push: true
        tags: myuser/ai-app:latest
        # 为AI应用优化构建缓存
        cache-from: type=gha
        cache-to: type=gha,mode=max

  deploy:
    needs: build-and-push
    runs-on: ubuntu-latest
    steps:
    - name: Deploy to production
      run: |
        echo "Deploying AI application to production..."
```

## AI应用监控实践

### 为AI应用自定义指标
```python
# ai_metrics.py - AI应用指标收集示例
from prometheus_client import Counter, Histogram, Gauge
import time

# AI API调用计数器
ai_api_calls = Counter('ai_api_total', 'Total AI API calls', ['endpoint'])
ai_response_time = Histogram('ai_response_time_seconds', 'AI response time', ['endpoint'])
ai_tokens_used = Counter('ai_tokens_total', 'Total tokens used', ['model'])

def ai_api_wrapper(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        ai_api_calls.labels(endpoint=func.__name__).inc()

        try:
            result = func(*args, **kwargs)
            return result
        finally:
            response_time = time.time() - start_time
            ai_response_time.labels(endpoint=func.__name__).observe(response_time)
    return wrapper
```

## 学习资源推荐

### AI部署资源 (重点)
- **模型服务**:
  - [vLLM Documentation](https://vllm.readthedocs.io/) - 高性能模型推理
  - [TGI (Text Generation Inference)](https://github.com/huggingface/text-generation-inference) - 文本生成推理
- **向量数据库部署**:
  - [pgvector部署指南](https://github.com/pgvector/pgvector) - PostgreSQL向量扩展
  - [Pinecone部署最佳实践](https://www.pinecone.io/learn/vector-database/) - 云端向量数据库

### 通用DevOps资源
- **Docker 与容器化**:
  - [Docker 官方文档](https://docs.docker.com/)
  - 《Docker 从入门到实践》
- **CI/CD**:
  - [GitHub Actions 官方文档](https://docs.github.com/cn/actions)
- **监控与日志**:
  - [Prometheus 官方文档](https://prometheus.io/docs/)
  - [Grafana 官方文档](https://grafana.com/docs/)

### AI应用运维资源
- 《AI系统工程化实践》- AI应用运维指南
- [OpenCost](https://www.opencost.io/) - 云成本监控工具
- [Kubeflow](https://www.kubeflow.org/) - 机器学习在Kubernetes上的应用

## 实践项目 (第15-16周里程碑)

### 项目1: AI应用容器化 (第15周目标)
- 为你的AI知识库系统编写优化的Dockerfile
- 创建完整的Docker Compose配置
- 配置向量数据库服务
- 优化镜像大小和构建时间

### 项目2: CI/CD流水线 (第15周目标)
- 设置GitHub Actions自动化流程
- 配置自动化测试 (功能测试 + AI质量测试)
- 实现安全扫描和质量检查
- 设置自动化部署

### 项目3: 监控和部署 (第16周目标)
- 集成Prometheus指标收集
- 配置Grafana仪表板展示AI指标
- 部署应用到云平台
- 实现成本监控和告警

## 学习重点

- **掌握AI应用特有的部署需求** (模型服务、向量数据库等)
- **实施AI应用性能监控** (响应时间、准确性、成本)
- **优化AI服务资源使用** (成本控制、性能平衡)
- **确保AI应用安全性** (API密钥、提示注入防护等)
- **理解AI运维特殊考虑** (模型版本、响应质量等)
- **建立完整的DevOps流程** (从代码到生产)