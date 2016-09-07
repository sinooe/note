# sublime
## markdown配置
### 安装插件管理 Package Control
1.  ctrl+` 或者 View > Show Console 菜单打开控制台
2. 粘贴对应版本的代码后回车安装

* 适用于 Sublime Text 3：

```
import  urllib.request,os;pf='Package Control.sublime-package';ipp=sublime.installed_packages_path();urllib.request.install_opener(urllib.request.build_opener(urllib.request.ProxyHandler()));open(os.path.join(ipp,pf),'wb').write(urllib.request.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read())
```

* 适用于 Sublime Text 2：

```
import  urllib2,os;pf='Package Control.sublime-package';ipp=sublime.installed_packages_path();os.makedirs(ipp)ifnotos.path.exists(ipp)elseNone;urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler()));open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read());print('Please restart Sublime Text to finish installation')
```

## 插件
### [MarkdownEditing](https://github.com/SublimeText-Markdown/MarkdownEditing)
* 作用不大，可以不安装
* 语法高亮
* command + option + k 插入链接
* command + shift + k 插入图片

### [OmniMarkupPreviewer](https://github.com/timonwong/OmniMarkupPreviewer)
* 可以局域网内部实时预览，但不能支持待办事项
* Command +Option +O: 在浏览器中预览
* Command+Option+X: 导出HTML
* Ctrl+Alt+C: HTML标记拷贝至剪贴板
* 配置OmniMarkupPreviewer.sublime-settings 文件
    "server_host":设置局域网访问IP，默认127.0.0.1
    "renderer_options-MarkdownRenderer"：渲染扩展项，[toc] 目录；strikeout 删除线；superscript 上标；subscript 下标；codehilite 代码块语法高亮支持

### [MarkdownPreview](https://github.com/revolunet/sublimetext-markdown-preview)
* 生成本地html后预览，支持待办事项
* 生成html文件：ctrl+B

### [SmartMarkdown](https://github.com/demon386/SmartMarkdown)
* 快捷键折叠文档
* 对于标题：TAB，折叠/打开对应标题区域
* 对于全局：SHIFT+TAB，整体折叠为一级标题
## 自定制代码片段(Code Snippets)


## sublime中文匹配通配符
```
[\x{4e00}-\x{9fa5}]
```

## sublime指南
- [ ] [http://www.kancloud.cn/digest/sublime-text-complete-guide/61431](http://www.kancloud.cn/digest/sublime-text-complete-guide/61431)
