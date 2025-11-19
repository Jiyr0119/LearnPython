"""
单词计数器程序
读取文本文件，统计单词出现频率
"""

import string
from collections import Counter

def read_file(filename):
    """读取文件内容"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"错误：文件 '{filename}' 不存在。")
        return None
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return None

def count_words(text):
    """统计单词频率"""
    # 转换为小写并移除标点符号
    text = text.lower()
    # 移除标点符号
    text = text.translate(str.maketrans('', '', string.punctuation))
    # 分割成单词列表
    words = text.split()
    
    # 使用Counter统计词频
    word_count = Counter(words)
    return word_count

def display_word_count(word_count, top_n=10):
    """显示词频统计结果"""
    print(f"\n前 {top_n} 个最常出现的单词:")
    print("-" * 30)
    for word, count in word_count.most_common(top_n):
        print(f"{word}: {count}")

def create_sample_file():
    """创建示例文本文件"""
    sample_text = """
    Python is a high-level programming language. 
    It is widely used for web development, data analysis, artificial intelligence, and scientific computing.
    Python's simple syntax and readability make it a great choice for beginners.
    Many developers love Python because of its versatility and extensive library support.
    Whether you're building a website, analyzing data, or creating machine learning models, Python has you covered.
    """
    
    with open('sample.txt', 'w', encoding='utf-8') as file:
        file.write(sample_text)
    print("已创建示例文件 'sample.txt'")

def main():
    """主程序"""
    print("欢迎使用单词计数器")
    
    # 询问用户是否需要创建示例文件
    create_sample = input("是否需要创建示例文件? (y/n): ").lower()
    if create_sample == 'y':
        create_sample_file()
    
    # 获取文件名
    filename = input("请输入要分析的文本文件名: ")
    
    # 读取文件
    text = read_file(filename)
    if text is None:
        return
    
    # 统计单词
    word_count = count_words(text)
    
    # 显示结果
    display_word_count(word_count)
    
    # 显示总单词数
    print(f"\n总单词数: {sum(word_count.values())}")
    print(f"不重复单词数: {len(word_count)}")

if __name__ == "__main__":
    main()