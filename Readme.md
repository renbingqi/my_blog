# My Blog 系统

## 主要功能 

1. 可以在网页上发布博客文章（包括增删改查）
2. 对文章进行分类管理-专栏（通过专栏可以看到该专栏下所有的博客文章）
3. 文章热度
4. 个人简介-关于
5. 友链
6. 搜索功能

## 接口

### 文章

- 创建文章

  ```
  {{Base_url}}/articles/create
  ```

- 删除文章

  ```
  {{Base_url}}/articles/delete/{{article_id}}
  ```

- 更新文章

  ```
  {{Base_url}}/articles/update/{{article_id}}
  ```

- 文章列表

  ```
  {{Base_url}}/articles
  ```

  

### 专栏

- 专栏创建

  ```
  {{Base_url}}/classification/create
  ```

- 删除专栏

  ```
  {{Base_url}}/classification/delete/{{classification_id}}
  ```

- 修改专栏

  ```
  {{Base_url}}/classification/update/{{classification_id}}
  ```

- 专栏

  ```
  {{Base_url}}/classifications
  ```

### 热度

```
{{Base_url}}/articles/hot/{{article_id}}
```