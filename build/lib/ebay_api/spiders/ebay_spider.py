import scrapy
import dateparser


class CardSpider(scrapy.Spider):
    name = "cards"
    start_urls = [
        "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=2018+baker+mayfield+psa+10+auto&_sacat=0&LH_TitleDesc=0&LH_Auction=1&_osacat=0&_odkw=2018+josh+allen+psa+10+auto&LH_Complete=1&rt=nc&LH_Sold=1&_ipg=100",
        "https://www.ebay.com/sch/i.html?_from=R40&_nkw=2018+josh+allen+psa+10+auto&_sacat=0&LH_Sold=1&LH_Complete=1&rt=nc&LH_Auction=1&_ipg=100",
        "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=2018+josh+rosen+psa+10+auto&_sacat=0&LH_TitleDesc=0&LH_Auction=1&_osacat=0&_odkw=2018+lamar+jackson+psa+10+auto&LH_Complete=1&LH_Sold=1",
        "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=2018+lamar+jackson+psa+10+auto&_sacat=0&LH_TitleDesc=0&LH_Auction=1&_osacat=0&_odkw=2018+sam+darnold+psa+10+auto&LH_Complete=1&LH_Sold=1",
        "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=2018+sam+darnold+psa+10+auto&_sacat=0&LH_TitleDesc=0&LH_Auction=1&_osacat=0&_odkw=2018+baker+mayfield+psa+10+auto&LH_Complete=1&LH_Sold=1",
    ]

    def sitemap_filter(self, entries):
        for entry in entries:
            date_time = datetime.strptime()

    def parse(self, response):
        for products in response.xpath('//div/div/ul/li[contains(@class, "s-item" )]'):
            yield {
                "Title": products.css(
                    "h3.s-item__title.s-item__title--has-tags::text"
                ).get(),
                "Sold_Date": dateparser.parse(
                    products.xpath(
                        './/*[@class="s-item__title--tagblock__COMPLETED"]//text()'
                    )
                    .get()
                    .replace("Sold  ", "")
                ).strftime("%Y-%m-%d"),
                "Sold_Price": products.xpath('.//*[@class="s-item__price"]//text()')
                .get()
                .replace("$", ""),
                "Bids": products.css("span.s-item__bids.s-item__bidCount::text")
                .get()
                .replace(" bids", "")
                .replace(" bid", ""),
                "Card_Link": products.css("a.s-item__link").attrib["href"],
                "Image_Link": products.css("img.s-item__image-img").attrib["src"],
            }
