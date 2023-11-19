#!/bin/python3

import math
import os
import random
import re
import sys


class TreeNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.height = 1
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def get(self, key):
        node = self.searchKey(self.root, key)
        if node is not None:
            return node.data
        else:
            return None

    def set(self, key, value):
        self.root = self.insertKey(self.root, key, value)

    def searchKey(self, node, key):
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node
        return None

    def nodeHeight(self, node):
        if not node:
            return 0
        return node.height

    def insertKey(self, node, key, value):
        if node is None:
            return TreeNode(key, value)
        elif key == node.key:
            node.value = value
            return node
        elif key < node.key:
            node.left = self.insertKey(node.left, key, value)
        else:
            node.right = self.insertKey(node.right, key, value)

        node.height = 1 + max(self.nodeHeight(node.left), self.nodeHeight(node.right))
        bal = self.nodeHeight(node.left) - self.nodeHeight(node.right)

        if bal > 1 and key < node.left.key:
            return self.rotateRight(node)
        if bal > 1 and key > node.left.key:
            node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)
        if bal < -1 and key > node.right.key:
            return self.rotateLeft(node)
        if bal < -1 and key < node.right.key:
            node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)

        return node

    def rotateLeft(self, z):
        y = z.right
        temp = y.left
        y.left = z
        z.right = temp

        z.height = 1 + max(self.nodeHeight(z.left), self.nodeHeight(z.right))
        y.height = 1 + max(self.nodeHeight(y.left), self.nodeHeight(y.right))
        return y

    def rotateRight(self, z):
        y = z.left
        temp = y.right
        y.right = z
        z.left = temp

        z.height = 1 + max(self.nodeHeight(z.left), self.nodeHeight(z.right))
        y.height = 1 + max(self.nodeHeight(y.left), self.nodeHeight(y.right))
        return y

    def traverse(self, node, nodesList):
        if node is None:
            return
        self.traverse(node.left, nodesList)
        nodesList.append(node)
        self.traverse(node.right, nodesList)

    def getNodesList(self):
        nodesList = []
        self.traverse(self.root, nodesList)
        return nodesList


class Set:
    def __init__(self):
        self.tree = Tree()

    def add(self, value):
        self.tree.set(value, object())

    def __contains__(self, value):
        key = self.tree.get(value)
        return key is not None

    def getItemsList(self):
        nodes = self.tree.getNodesList()
        return [node.key for node in nodes]

class InvertedIndex:
    def __init__(self):
        self.indexes = Tree()
        self.unique_words = 0
        self.all_words = 0

    def index_document(self, document, document_id):
        words = document.split()
        for word in words:
            docs = self.indexes.get(word)
            if docs is None:
                docs = Set()
                self.indexes.set(word, docs)
                self.unique_words += 1

            if document_id not in docs:
                self.all_words += 1
                docs.add(i)

    def search(self, word):
        answer = self.indexes.get(word)
        if answer is not None:
            return answer.getItemsList()
        else:
            return {-1}

    def get_average_documents_per_key(self):
        return round(self.all_words / self.unique_words)

    def get_keys(self):
        nodes = self.indexes.getNodesList()
        return [node.key for node in nodes]


if __name__ == '__main__':
    num_documents = int(input().strip())

    documents = []

    for _ in range(num_documents):
        documents_item = input()
        documents.append(documents_item)

    num_queries = int(input().strip())

    queries = []

    for _ in range(num_queries):
        queries_item = input()
        queries.append(queries_item)

    invertedIndex = InvertedIndex()

    for i in range(num_documents):
        invertedIndex.index_document(documents[i], i)

    for query in queries:
        docs = invertedIndex.search(query)
        for doc in docs:
            print(doc, end=' ')
        print()

    print(invertedIndex.get_average_documents_per_key())

    try:
        print_keys_flag = input()
        should_print_keys = print_keys_flag == 'print_keys'
    except:
        should_print_keys = False

    if should_print_keys:
        words = invertedIndex.get_keys()
        for word in words:
            print(word, end=' ')

