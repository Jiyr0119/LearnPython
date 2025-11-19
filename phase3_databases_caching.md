# 第三阶段：深入学习数据库与缓存

在掌握了 Python 后端开发框架之后，下一步是深入学习数据库和缓存技术。作为全栈开发者，理解数据存储和访问机制对于构建高性能应用至关重要。

## 数据库基础

### 关系型数据库 (SQL)
关系型数据库使用结构化查询语言(SQL)进行数据管理，数据以表格形式存储，具有严格的模式(schema)。

**主要特点**:
- ACID 特性保证数据一致性
- 支持复杂查询和关联操作
- 成熟稳定，有丰富的工具支持

**常用数据库**:
- **PostgreSQL**: 功能强大，开源，支持复杂数据类型和扩展
- **MySQL**: 流行的关系型数据库，广泛应用于 Web 应用
- **SQLite**: 轻量级数据库，适合小型应用和移动设备

### 非关系型数据库 (NoSQL)
NoSQL 数据库不使用传统的表格关系模型，而是采用键值对、文档、列族或图等数据模型。

**主要特点**:
- 灵活的数据模型
- 易于水平扩展
- 高性能读写

**常用数据库**:
- **MongoDB**: 文档数据库，适合存储 JSON 格式的文档数据
- **Redis**: 键值存储数据库，以内存存储为主，常用于缓存和消息队列

## 学习内容

### SQL 数据库
1. **基础概念**
   - 数据库、表、字段、记录的概念
   - 主键、外键、索引的作用
   - 数据类型和约束

2. **SQL 语言**
   - DDL (数据定义语言): CREATE, ALTER, DROP
   - DML (数据操作语言): INSERT, UPDATE, DELETE
   - DQL (数据查询语言): SELECT, JOIN, 子查询
   - DCL (数据控制语言): GRANT, REVOKE

3. **数据库设计**
   - 实体关系模型(ER Model)
   - 范式化设计
   - 数据库规范化

4. **Python 集成**
   - 使用 psycopg2 或 asyncpg 连接 PostgreSQL
   - 使用 mysql-connector-python 或 PyMySQL 连接 MySQL
   - 使用 SQLAlchemy 作为 ORM 工具

### NoSQL 数据库
1. **MongoDB**
   - 文档模型和 BSON 格式
   - CRUD 操作
   - 索引和聚合管道
   - Python 驱动 pymongo 的使用

2. **Redis**
   - 数据结构: String, Hash, List, Set, Sorted Set
   - 持久化机制
   - 发布/订阅模式
   - Python 客户端 redis-py 的使用

## 缓存技术

缓存是提高应用性能的重要手段，特别是在高并发场景下。

### Redis 作为缓存
1. **缓存策略**
   - Cache-Aside Pattern
   - Write-Through 和 Write-Behind
   - 缓存失效策略

2. **实际应用**
   - 会话存储
   - 页面缓存
   - 分布式锁
   - 限流控制

### 其他缓存方案
- **Memcached**: 传统的分布式内存对象缓存系统
- **应用层缓存**: 使用 Python 的 functools.lru_cache 等

## 学习资源推荐

### SQL 数据库
- **书籍**:
  - 《SQL必知必会》- 简明易懂的 SQL 入门书
  - 《高性能MySQL》- 深入理解 MySQL 的经典著作
- **在线教程**:
  - [W3Schools SQL Tutorial](https://www.w3schools.com/sql/) - 免费的 SQL 在线教程
  - [SQLZOO](https://sqlzoo.net/) - 交互式 SQL 练习平台
- **实践平台**:
  - [LeetCode 数据库题目](https://leetcode.cn/problemset/database/) - 通过刷题掌握 SQL

### NoSQL 数据库
- **MongoDB**:
  - [MongoDB 官方文档](https://docs.mongodb.com/manual/) - 权威参考资料
  - [MongoDB University](https://university.mongodb.com/) - 免费的在线课程
- **Redis**:
  - [Redis 官方文档](https://redis.io/documentation) - 完整的文档资源
  - [Redis 命令参考](http://redisdoc.com/) - 中文版命令手册

### Python 数据库集成
- **SQLAlchemy**:
  - [SQLAlchemy 官方文档](https://docs.sqlalchemy.org/) - ORM 框架的权威指南
  - [Essential SQLAlchemy](https://www.oreilly.com/library/view/essential-sqlalchemy-2nd/9781491916544/) - 深入学习 SQLAlchemy 的书籍
- **数据库驱动**:
  - psycopg2, PyMySQL, pymongo, redis-py 等官方文档

## 实践项目

1. **电商系统数据库设计**:
   - 设计用户、商品、订单等核心表结构
   - 实现商品搜索、订单查询等功能
   - 使用 SQLAlchemy 进行 ORM 映射

2. **博客系统 MongoDB 版**:
   - 使用 MongoDB 存储文章、评论等数据
   - 实现标签分类、全文搜索功能
   - 对比与 SQL 数据库的差异

3. **Redis 缓存应用**:
   - 实现热点数据缓存
   - 使用 Redis 实现排行榜功能
   - 实现分布式会话管理

## 学习重点

- 理解不同数据库类型的适用场景
- 掌握 SQL 查询优化技巧
- 学会使用索引提高查询性能
- 理解事务和并发控制机制
- 掌握缓存策略和最佳实践
- 了解数据库备份和恢复方案