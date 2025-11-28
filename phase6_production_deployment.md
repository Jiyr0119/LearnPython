# 第六阶段：生产部署与DevOps

在掌握了 Python 基础、Web框架、数据库和缓存技术之后，学习如何将应用部署到生产环境至关重要。这一阶段将帮助你掌握现代应用部署技术和实践，为后续的RAG项目部署打下坚实基础。

## 学习内容

### 1. 容器化技术 (Docker)
- Docker 基础概念和原理
- Dockerfile 编写最佳实践
- 多阶段构建优化镜像大小
- Docker Compose 多服务编排
- 容器安全最佳实践
- 镜像版本管理和发布策略

### 2. 部署策略与环境管理
- 云平台选择 (AWS, GCP, Azure, 阿里云等)
- 环境隔离 (开发/测试/生产)
- CI/CD 流水线设置 (GitHub Actions, GitLab CI)
- 零停机部署策略 (蓝绿部署、滚动更新)
- 配置管理与环境变量

### 3. 监控与日志 (Observability)
- 应用性能监控 (APM) - Prometheus + Grafana
- 日志收集与分析 - ELK Stack (Elasticsearch, Logstash, Kibana) 或 Loki
- 错误追踪 - Sentry 或类似工具
- 健康检查与告警
- 指标收集与可视化

### 4. 性能优化
- Web服务器优化 (Nginx, Apache)
- 反向代理配置
- 负载均衡策略
- 缓存策略 (浏览器缓存、CDN)
- 数据库连接池优化
- 应用性能分析

### 5. 安全实践 (重点加强)
- 容器安全扫描
- 依赖包漏洞扫描
- HTTPS/TLS 配置
- API 认证与授权 (JWT, OAuth2)
- 网络安全 (防火墙、VPC)
- 安全凭证管理 (HashiCorp Vault, AWS Secrets Manager)

### 6. AI/RAG应用特殊考虑 (为下一阶段做准备)
- GPU资源管理 (如适用)
- 模型服务部署策略 (vLLM, TGI)
- 批处理与流处理优化
- 响应时间优化
- 模型版本管理

## 容器化实践 (重点)

### Dockerfile 最佳实践
```dockerfile
# 多阶段构建示例
# 构建阶段
FROM python:3.11-slim as builder
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && \
    poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt

# 运行阶段
FROM python:3.11-slim
RUN useradd --create-home --shell /bin/bash app
WORKDIR /home/app
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*
COPY --chown=app:app . .
USER app
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose 配置
```yaml
# docker-compose.yml 示例
version: "3.8"
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/myapp
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis
    volumes:
      - ./data:/app/data
  
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

volumes:
  postgres_data:
  redis_data:
```

## CI/CD 实践

### GitHub Actions 示例
```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

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
        tags: myuser/myapp:latest
```

## 监控与日志实践

### 应用指标监控
- 集成 Prometheus 客户端收集自定义指标
- 使用中间件跟踪请求延迟和错误率
- 监控数据库连接池状态
- 跟踪 API 调用频率和响应时间

### 日志管理
- 结构化日志记录 (JSON格式)
- 日志级别管理 (DEBUG, INFO, WARNING, ERROR)
- 敏感信息过滤 (密码、密钥等)

## 学习资源推荐

### Docker 与容器化
- [Docker 官方文档](https://docs.docker.com/)
- 《Docker 从入门到实践》
- [Docker Bench for Security](https://github.com/docker/docker-bench-security)

### CI/CD
- [GitHub Actions 官方文档](https://docs.github.com/cn/actions)
- [GitLab CI/CD 文档](https://docs.gitlab.com/ee/ci/)
- 《持续交付：发布可靠软件的系统方法》

### 监控与日志
- [Prometheus 官方文档](https://prometheus.io/docs/)
- [Grafana 官方文档](https://grafana.com/docs/)
- [ELK Stack 官方文档](https://www.elastic.co/guide/index.html)

### 云平台
- 各大云厂商官方文档和教程
- 《云原生应用架构实践》

## 实践项目

1. **Docker化现有项目**:
   - 为你的全栈项目编写 Dockerfile
   - 使用 Docker Compose 管理多服务
   - 优化镜像大小和构建时间

2. **CI/CD 流水线**:
   - 为项目设置自动化测试
   - 配置自动化构建和部署
   - 实现安全扫描和质量检查

3. **监控系统**:
   - 集成 Prometheus 指标收集
   - 配置 Grafana 仪表板
   - 设置告警规则

4. **生产部署**:
   - 将应用部署到云平台
   - 配置域名和 SSL 证书
   - 实现健康检查和自动恢复

## 学习重点

- 掌握容器化技术，理解其优势和最佳实践
- 学会配置和管理 CI/CD 流水线
- 理解可观测性的重要性，掌握监控和日志最佳实践
- 重视安全实践，保护应用和数据
- 了解成本控制和资源优化
- 准备好将 AI/RAG 应用部署到生产环境