#!/usr/bin/env python
import re
import os.path
import time
import markdown
from glob import glob

class Blog:
    _posts_path = './posts/'
    _all_posts = []
    _all_tags = {}

    def md2html(self, mdstr):
        exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.tables', 'markdown.extensions.toc']
        md = markdown.Markdown(extensions=exts)
        content = md.convert(mdstr)
        toc = md.toc
        return toc, content

    def __find_files(self, directory, extension):
        files = glob('{}/*.{}'.format(directory, extension))
        return files

    def __get_all_posts(self):
        if not self._all_posts:
            _files = []
            post_files = self.__find_files(self._posts_path, 'md')
            for file in post_files:
                with open(file) as f:
                    fcontents = f.readlines()

                pattern = re.compile(r'^\s*(title|author|date|position|toc|intro|status|tags)\s*:(.*?)$', re.I)
                content_line_num = 0
                post_title = ''
                post_intro = ''
                post_author = ''
                post_date = ''
                post_status = ''
                post_tags = []
                position = 0
                toc = False
                for index, line in enumerate(fcontents):
                    if (':' in line):
                        match = pattern.match(line)
                        if not match:
                            content_line_num = index
                            break
                        else:
                            head = match.group(1).lower()
                            content = match.group(2).strip()
                            if head == 'title':
                                post_title = content
                            elif head == 'author':
                                post_author = content
                            elif head == 'date':
                                post_date = content
                            elif head == 'position':
                                position = int(time.time()) - int(content)
                            elif head == 'toc':
                                toc = True if content.lower() == 'yes' else False
                            elif head == 'intro':
                                post_intro = content
                            elif head == 'status':
                                post_status = 'public' if content.lower() == 'public' else 'draft'
                            elif head == 'tags':
                                post_tags = list(filter(None, re.split(',|\s+', content)))
                    else:
                        content_line_num = index
                        break

                if post_status != 'public':
                    continue
                for tag in post_tags:
                    if (self._all_tags.get(tag)):
                        self._all_tags[tag] += 1
                    else:
                        self._all_tags[tag] = 1
                if post_date:
                    post_time = time.mktime(time.strptime(post_date, '%Y-%m-%d'))
                else:
                    post_time = os.path.getmtime(file)
                post_content = ''.join(fcontents[content_line_num:]).strip()
                if not post_intro:
                    post_text = re.sub(r'<[^>]*?>', '', self.md2html(post_content))
                    post_intro = post_text[:200]
                slug = re.sub(r'.md$', '', os.path.basename(file))
                _files.append({
                    'fname': file,
                    'slug': slug,
                    'toc': toc,
                    'link': '/post/{}'.format(slug),
                    'title': post_title,
                    'date': time.strftime('%Y-%m-%d', time.localtime(post_time)),
                    'tags': post_tags,
                    'status': post_status,
                    'intro': post_intro,
                    'content': post_content,
                    'position': position if position else post_time
                });

            self._all_posts = sorted(_files, key=lambda k:k['position'], reverse=True)
        return self._all_posts

    def get_post(self, slug):
        current_post = {}
        prev_post = {}
        next_post = {}
        posts = self.__get_all_posts()
        for index,post in enumerate(posts):
            if post['slug'] == slug:
                current_post = post
                if index > 0:
                    prev_post = posts[index-1]
                if index < len(posts)-1:
                    next_post = posts[index+1]
                current_post['html_toc'], current_post['html_content'] = self.md2html(post['content'])
                break
        return prev_post, current_post, next_post

    def get_posts(self):
        return self.__get_all_posts()

if __name__ == '__main__':
    blog = Blog()
    # print(blog.get_post('english'))
