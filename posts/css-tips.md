# CSS 小技巧

> 发表于 2026-02-15

分享一些实用的 CSS 技巧。

## 1. 居中元素

```css
.center {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

## 2. 响应式字体

```css
h1 {
  font-size: clamp(1.5rem, 5vw, 3rem);
}
```

## 3. 渐变文字

```css
.gradient-text {
  background: linear-gradient(135deg, #667eea, #764ba2);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

更多技巧待补充...
