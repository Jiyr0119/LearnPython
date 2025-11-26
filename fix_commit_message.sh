#!/bin/bash

# 修改 Git commit 信息的简单方法
# 适用于修改非最新的 commit

echo "🔧 修改 Git Commit 信息"
echo "========================"
echo ""
echo "目标 commit: d8b0136"
echo "当前信息: [提交内容简短描述]"
echo ""

# 方法 1: 使用 git rebase -i (交互式)
echo "📝 方法 1: 交互式 rebase (推荐)"
echo "运行以下命令:"
echo ""
echo "  GIT_SEQUENCE_EDITOR=\"sed -i '' 's/^pick d8b0136/reword d8b0136/'\" git rebase -i d98dab6"
echo ""
echo "然后 Git 会打开编辑器让你修改 commit 信息"
echo ""
echo "建议的新信息:"
echo "---"
echo "feat: Add set operations demonstration script"
echo ""
echo "Add comprehensive Python script demonstrating set operations including:"
echo "- Set creation and basic operations"
echo "- Set methods (add, remove, discard, pop, clear)"  
echo "- Set operations (union, intersection, difference, symmetric difference)"
echo "- Practical examples and use cases"
echo "---"
echo ""
echo "⚠️  注意事项:"
echo "1. 这会重写 Git 历史"
echo "2. 如果已推送到远程,需要 git push --force"
echo "3. 如果有协作者,请先沟通"
echo ""
echo "是否继续? (y/n)"
read -r response

if [ "$response" = "y" ] || [ "$response" = "Y" ]; then
    echo ""
    echo "🚀 开始 rebase..."
    
    # 创建临时的 commit message 文件
    cat > /tmp/new_commit_msg.txt << 'EOF'
feat: Add set operations demonstration script

Add comprehensive Python script demonstrating set operations including:
- Set creation and basic operations
- Set methods (add, remove, discard, pop, clear)
- Set operations (union, intersection, difference, symmetric difference)
- Practical examples and use cases
EOF
    
    # 使用环境变量设置编辑器
    export GIT_SEQUENCE_EDITOR="sed -i '' 's/^pick d8b0136/edit d8b0136/'"
    
    # 开始 rebase
    git rebase -i d98dab6
    
    # 如果进入了 edit 模式,修改 commit 信息
    if [ $? -eq 0 ]; then
        git commit --amend -F /tmp/new_commit_msg.txt
        git rebase --continue
        
        echo ""
        echo "✅ Commit 信息已修改!"
        echo ""
        echo "查看结果:"
        git log --oneline -5
        
        echo ""
        echo "如果需要推送到远程:"
        echo "  git push --force-with-lease origin $(git branch --show-current)"
    fi
    
    # 清理临时文件
    rm -f /tmp/new_commit_msg.txt
else
    echo "❌ 操作已取消"
fi
