# 第四阶段：学习前端基础（复习）

作为从前端全栈工程师转型的开发者，你已经具备了前端开发的基础知识。这一阶段的目标是复习和巩固前端核心技术，并了解如何与 Python 后端进行有效交互。

## 复习内容

### HTML (HyperText Markup Language)
HTML 是构建网页内容结构的标准标记语言。

**核心概念**:
- 文档结构 (DOCTYPE, html, head, body)
- 常用标签 (div, span, p, a, img, form, input, button等)
- 语义化标签 (header, nav, main, section, article, footer等)
- 表单处理和验证

### CSS (Cascading Style Sheets)
CSS 用于控制网页的样式和布局。

**核心概念**:
- 选择器 (元素选择器、类选择器、ID选择器、伪类等)
- 盒模型 (margin, border, padding, content)
- 布局技术 (Flexbox, Grid)
- 响应式设计 (媒体查询)
- CSS 预处理器 (Sass, Less)

### JavaScript
JavaScript 是实现网页交互功能的编程语言。

**核心概念**:
- 基本语法和数据类型
- 函数和作用域
- DOM 操作
- 事件处理
- 异步编程 (Promise, async/await)
- ES6+ 新特性 (箭头函数、模板字符串、解构赋值等)

## 前后端交互

### HTTP 协议
理解 HTTP 协议是前后端交互的基础。

**关键概念**:
- 请求方法 (GET, POST, PUT, DELETE等)
- 状态码 (200, 404, 500等)
- 请求头和响应头
- Cookie 和 Session

### RESTful API
RESTful 是一种网络应用程序的设计风格和开发方式。

**设计原则**:
- 使用标准的 HTTP 方法
- 无状态性
- 统一接口
- 资源导向

### 前端与 Python 后端交互
1. **使用 Fetch API 或 Axios 发送 HTTP 请求**
2. **处理 JSON 格式的数据**
3. **理解跨域问题及解决方案**
4. **掌握前端路由与后端路由的区别**

## 现代前端框架简介

虽然本项目重点是 Python 后端开发，但了解现代前端框架有助于全栈协作。

### React
- 组件化开发思想
- JSX 语法
- 状态管理 (useState, useEffect)
- 虚拟 DOM

### Vue.js
- 渐进式框架
- 模板语法
- 响应式数据绑定
- 组件系统

## AI 时代的前端技术 (新增 - 重点)

### 1. 快速原型开发工具
对于 AI 工程师来说，快速展示模型效果至关重要。
- **Streamlit**: 纯 Python 编写数据应用，极其适合快速构建 RAG 演示和数据仪表盘。
- **Gradio**: 专注于机器学习模型的演示界面，几行代码即可生成 Web UI。

### 2. 流式响应与实时交互
AI 应用（如 ChatGPT）的标志性体验。
- **Server-Sent Events (SSE)**: 处理 LLM 的流式输出 (Streaming Response)。
- **WebSocket**: 实现更复杂的双向实时通信。
- **Markdown 渲染**: 前端实时渲染 Markdown 内容 (如 `react-markdown`)。

## 学习资源推荐

### HTML/CSS/JavaScript 复习
- **MDN Web Docs**:
  - [HTML 基础](https://developer.mozilla.org/zh-CN/docs/Learn/HTML)
  - [CSS 基础](https://developer.mozilla.org/zh-CN/docs/Learn/CSS)
  - [JavaScript 指南](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide)
- **在线教程**:
  - [freeCodeCamp](https://www.freecodecamp.org/chinese/) - 免费的编程学习平台
  - [W3Schools](https://www.w3schools.com/) - 简明的 Web 技术教程

### 前后端交互
- **书籍**:
  - 《深入浅出Node.js》- 理解 JavaScript 在后端的应用
  - 《RESTful Web APIs》- 学习 RESTful API 设计
- **实践平台**:
  - [Postman](https://www.postman.com/) - API 测试工具
  - [JSONPlaceholder](https://jsonplaceholder.typicode.com/) - 虚拟 REST API 用于测试

## 实践项目

1. **创建一个简单的前端页面**:
   - 使用 HTML 构建页面结构
   - 使用 CSS 美化页面样式
   - 使用 JavaScript 实现简单的交互功能

2. **与 Python 后端 API 交互**:
   - 使用 FastAPI 创建一个简单的 RESTful API
   - 在前端页面中通过 Fetch API 调用后端接口
   - 实现数据的增删改查功能

3. **构建一个完整的前后端分离应用**:
   - 前端使用 HTML/CSS/JavaScript 构建用户界面
   - 后端使用 Python 框架提供 API 服务
   - 实现用户注册、登录、数据展示等功能

## 学习重点

- 复习并巩固前端基础知识
- 理解前后端分离架构的优势
- 掌握 RESTful API 的设计原则
- 学会使用工具调试前后端交互问题
- 了解现代前端框架的基本概念
- API优先(Design-First)开发模式 (利用你已有的前端经验设计更好的API)
- 前端与AI后端服务的交互模式 (特别是流式响应和实时数据)
- 使用OpenAPI规范设计API接口