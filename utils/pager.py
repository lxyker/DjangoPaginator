import math


class PageInfo(object):

    def __init__(self, current_page, all_count, per_page, show_page):
        """

        :param current_page: 当前页码
        :param all_count: 数据总个数
        :param per_page: 每页显示的个数
        :param show_page: 规定显示多少个页码
        """

        try:
            self.current_page = int(current_page)
        except Exception as e:
            self.current_page = 1
        if self.current_page < 1:
            self.current_page = 1

        self.per_page = per_page
        self.all_count = all_count
        self.all_pager = math.ceil(self.all_count / self.per_page)
        self.show_page = show_page

    def start(self):
        return (self.current_page - 1) * self.per_page

    def stop(self):
        return self.current_page * self.per_page

    def pager(self):
        s = str()

        half = int(self.show_page/2)

        # 如果总数据比较少，导致：self.all_pager < self.show_page
        if self.all_pager <= self.show_page:
            begin = 1
            end = self.all_pager + 1
        else:

            # 如果当前页比较靠前，比如self.current_page = 1之类
            if self.current_page <= half:
                begin = 1
                end = self.show_page + 1

            # 如果当前页比较靠后：
            elif self.current_page > self.all_pager - half:
                begin = self.all_pager - self.show_page + 1
                end = self.all_pager + 1

            # 中间情况：
            else:
                begin = self.current_page - half
                end = self.current_page + half + 1

        prev_page = "<li><a href='/app/custom/?page=%d'>上一页</a></li>" % (self.current_page - 1 if self.current_page > 1 else 1)
        s += prev_page

        for i in range(begin, end):
            if i == self.current_page:
                temp = "<li class='active'><a href='/app/custom/?page=%d'>%d</a></li>" % (i, i)
            else:
                temp = "<li><a href='/app/custom/?page=%d'>%d</a></li>" % (i, i)
            s += temp

        next_page = "<li><a href='/app/custom/?page=%d'>下一页</a></li>" % (
            self.current_page + 1 if self.current_page < self.all_pager else self.all_pager)

        s += next_page

        return s