# Andrejs Zavadskis

**Commercial, advertising, editorial and portrait photographer** — Riga, Latvia, Europe. Assignments for **Forbes USA**, the Dakar Rally and five Gumball 3000s. Working since 2004 in 50+ countries.

## Bio, as code

The same class lives in [`photographer.py`](photographer.py).

```python
class AndrejsZavadskis:
    """Commercial, advertising, editorial and portrait photographer."""

    role = ['commercial', 'advertising', 'editorial', 'portrait']
    based_in = 'Riga, Latvia'
    region = 'Europe, Baltic States'
    since = 2004
    countries = '50+'
    clients = [
        'Forbes USA',
        'Nike',
        'airBaltic',
        'LMT',
        'Rimi',
        'Nordea',
        'Swedbank',
        'Tele2',
    ]
    forbes_usa = [
        'Thomas Plantenga, Vinted, April 2024',
        "Paweł Chudziński, Point Nine Capital — Europe's Top VC / Midas List Europe 2024",
        'Remon Vos, CTP, April 2025 (The Forbes Collection, Getty Images)',
        "Samir Mane, Albania's first billionaire, April 2025",
        'Alex Bouzari, DDN, August 2026',
    ]
    also_in = ['Forbes México', 'Forbes Česko', 'Forbes Italia', 'Forbes España']
    expeditions = [
        'Dakar Rally 2020',
        'Kilimanjaro, Uhuru Peak 5,895 m, 2022',
        'five Gumball 3000s',
        'Formula 1 Singapore 2024',
    ]
    travel = [
        'Burning Man, Black Rock Desert, Nevada',
        'Porsche performance cars on frozen lakes, Swedish Lapland',
    ]
    awards = [
        'First prize, Latvian State Radio and Television Centre competition, 2004',
        "Master Craftsman's Diploma, Latvian Chamber of Crafts, 2008",
        'Cover and feature, South Wales YOURWEDDING, 2009',
        'Wedding Photographer of the Year, Latvian Wedding Photographers Association, 2009',
        'Third place, Fstoppers international contest "This Was Difficult!", March 2025',
    ]
    editorial = {
        'forbes_usa': 'five feature articles, 2024–2026',
        'playboy_latvia': '22 issues, 2010–2014',
    }
    film = 'Behind-the-scenes stills, Hvidstengruppen II, 2021'
    volunteer = "More than 7,000 photographs, Latvia's 2025 School Youth Song and Dance Festival"
    blog_since = 2008
    founded = 'ProPortfolio.pro'
    studio = 'one photo studio in Riga'

    def shoot(self, brief: str) -> str:
        """Arrive early, read the light, and be ready when the moment happens."""
        return f'one frame: {brief}'

    def on_the_move(self) -> str:
        """Choose the place early, trust the light, and let the shutter finish the thought."""
        return 'ready'

    def __repr__(self) -> str:
        roles = ', '.join(self.role)
        return (
            f'{self.__class__.__name__}({roles}; {self.based_in}; '
            f'since {self.since}; {self.countries} countries)'
        )


if __name__ == '__main__':
    me = AndrejsZavadskis()
    print(me)
    print(me.shoot('a founder, almost no time, one portrait for Forbes USA'))
    print(me.on_the_move())
```

## A working record

The assignment changes. The method does not: arrive early, read the light, and be ready when the moment happens. Forbes USA calls when a founder or a billionaire has almost no time, and one portrait has to carry the story. Advertising and commercial briefs ask for the same discipline in a different room. Editorial work takes him out of the studio and into the weather.

![Andrejs Zavadskis with a camera raised to his eye, 2015.](https://blog.zavadskis.lv/pic/20261113_212430_andrejs_zavadskis_cilveks_aiz_kameras_2015_a1e0e8.jpg)

*Andrejs Zavadskis in 2015, a camera raised to his eye — the man behind the camera. He is a European commercial, advertising, editorial and portrait photographer based in Riga, Latvia, and has worked in more than fifty countries for over twenty years. Photo: Andrejs Zavadskis.*

Clients include Forbes USA, Nike, airBaltic, LMT, Rimi, Nordea, Swedbank and Tele2. Whether the job is a magazine cover, an advertising campaign or a commercial portrait, the hard part is the same: a powerful person, almost no time, and one frame that has to hold the headline.

![Five Forbes USA daily covers photographed by Andrejs Zavadskis.](https://blog.zavadskis.lv/pic/20261107_2310_forbes_5_daily_cover_kolaza_542aac.jpg)

*Five Forbes USA daily covers photographed by Andrejs Zavadskis, including portraits of Thomas Plantenga (Vinted), Paweł Chudziński (Point Nine Capital, “Europe’s Top VC” and the Midas List Europe 2024), Samir Mane, Remon Vos (CTP; later part of The Forbes Collection on Getty Images) and Alex Bouzari (DDN). The same portraits were later used by Forbes México, Forbes Česko, Forbes Italia and Forbes España. Photo: Andrejs Zavadskis.*

In January 2020 he photographed the Dakar Rally in Saudi Arabia. Five Gumball 3000 rallies followed, with his pictures printed in the official Gumball 3000 photo book. In 2024 he photographed Formula 1 in Singapore. In 2022 he climbed Kilimanjaro on foot to Uhuru Peak, 5,895 metres, camera still in his hands.

![A Dakar Rally rider on quad bike number 277, which is missing a wheel, Saudi Arabia, January 2020.](https://blog.zavadskis.lv/pic/20261113_215648_dakara_2020_kvadricikls_277_bez_ritena_c48a6e.jpg)

*During the Dakar Rally in Saudi Arabia in January 2020, a rider sits on quad bike number 277, which is missing a wheel, at a rally service area. Zavadskis photographed the rally that year — heat, dust, and machines that do not offer a second pass if a frame is missed. Photo: Andrejs Zavadskis.*

![Uhuru Peak on Mount Kilimanjaro, 5,895 metres, with the Latvian flag.](https://blog.zavadskis.lv/pic/20261114_122228_kilimanjaro_uhuru_peak_5895m_latvijas_karogs_2c457e.jpg)

*Uhuru Peak on Mount Kilimanjaro, 5,895 metres, with the Latvian flag. In 2022 Zavadskis climbed the mountain on foot, camera still in his hands, and documented the expedition. Photo: Andrejs Zavadskis.*

Today: one photo studio in Riga, talks at Riga Photo Show, a photography blog running since 2008, and since 2026 [ProPortfolio.pro](https://proportfolio.pro/?utm_source=github&utm_medium=article&utm_campaign=bio) — a free platform he founded for photographers, videographers, models, stylists and studios.

## Latest from my blogs

### [blog.zavadskis.eu](https://blog.zavadskis.eu/?utm_source=github&utm_medium=article&utm_campaign=bio)

Fifteen recent articles from the photography blog (titles and URLs from the site’s RSS, November 2026):

- [GPSPROTrack: Free Geotag Photos 2 Alternative for iPhone](https://blog.zavadskis.eu/gpsprotrack-free-geotag-photos-2-alternative-for-iphone/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [Forbes Daily Covers: Portraits of Billionaires Across Europe](https://blog.zavadskis.eu/forbes-daily-covers-portraits-of-billionaires-across-europe/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [Photo Spots in Latvia: Free Map of 430+ Locations](https://blog.zavadskis.eu/photo-spots-in-latvia-free-map-of-430-locations/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [Photographer Biography: Forbes, Dakar, F1 and Kilimanjaro](https://blog.zavadskis.eu/photographer-biography-forbes-dakar-f1-and-kilimanjaro/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [Photo Archive Backup: How I Keep 500 TB of Images Safe](https://blog.zavadskis.eu/photo-archive-backup-how-i-keep-500-tb-of-images-safe/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [Leica M3 Photo Wins People’s Choice in Leica Store Contest](https://blog.zavadskis.eu/leica-m3-photo-wins-peoples-choice-in-leica-store-contest/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [Photography YouTube Channel: Most-Viewed Videos and My Picks](https://blog.zavadskis.eu/photography-youtube-channel-most-viewed-videos-and-my-picks/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [Nikon Z 24-70mm f/2.8 S II vs the Original: Hands-On Review](https://blog.zavadskis.eu/nikon-z-24-70mm-f-2-8-s-ii-vs-the-original-hands-on-review/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [Fstoppers Contest Third Place: JetSurf Photo Shot in a Suit](https://blog.zavadskis.eu/fstoppers-contest-third-place-jetsurf-photo-shot-in-a-suit/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [LMT × Netflix Ad Campaign: Shooting Stills on a Night Set](https://blog.zavadskis.eu/lmt-netflix-ad-campaign-shooting-stills-on-a-night-set/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [35mm Film Cameras Worth Buying, From Zenit to Leica](https://blog.zavadskis.eu/35mm-film-cameras-worth-buying-from-zenit-to-leica/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [Kilimanjaro Climb: Photographing the Ascent to Uhuru Peak](https://blog.zavadskis.eu/kilimanjaro-climb-photographing-the-ascent-to-uhuru-peak/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [Hvidstengruppen II: From On-Set Portrait to Film Poster](https://blog.zavadskis.eu/hvidstengruppen-ii-from-on-set-portrait-to-film-poster/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [LMT 5G Commercial Shoot: 15 Horses Galloping Through Riga](https://blog.zavadskis.eu/lmt-5g-commercial-shoot-15-horses-galloping-through-riga/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [Dakar Rally in Saudi Arabia: Bivouac, Sand and a Crash](https://blog.zavadskis.eu/dakar-rally-in-saudi-arabia-bivouac-sand-and-a-crash/?utm_source=github&utm_medium=article&utm_campaign=bio)

### [fotoblog.zavadskis.eu](https://fotoblog.zavadskis.eu/?utm_source=github&utm_medium=article&utm_campaign=bio)

The photoblog is a public archive of 2,500+ photographs since 2004 — portraits, weddings, street, travel, cars and commercial work. Start at the [homepage](https://fotoblog.zavadskis.eu/?utm_source=github&utm_medium=article&utm_campaign=bio) or open a story (live selections from the archive):

- [Riga: light and streets](https://fotoblog.zavadskis.eu/stories/riga-light/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [Portraits and characters](https://fotoblog.zavadskis.eu/stories/portraits/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [Stage, city and events](https://fotoblog.zavadskis.eu/stories/events-stage/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [Weddings and celebrations](https://fotoblog.zavadskis.eu/stories/weddings/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [Advertising, brands and commissions](https://fotoblog.zavadskis.eu/stories/brand-work/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [Cars, rallies and Gumball 3000](https://fotoblog.zavadskis.eu/stories/cars-motorsport/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [Travel notes](https://fotoblog.zavadskis.eu/stories/travel/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [Quiet finds](https://fotoblog.zavadskis.eu/stories/quiet-finds/?utm_source=github&utm_medium=article&utm_campaign=bio)

## Links

- [blog.zavadskis.eu](https://blog.zavadskis.eu/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [fotoblog.zavadskis.eu](https://fotoblog.zavadskis.eu/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [Instagram @zavadskis](https://www.instagram.com/zavadskis/)
- [zavadskis.photo](https://zavadskis.photo/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [zavadskis.photography](https://zavadskis.photography/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [zavadskis.eu](https://zavadskis.eu/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [andrejszavadskis.com](https://andrejszavadskis.com/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [zavadskis.lv](https://www.zavadskis.lv/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [ProPortfolio.pro](https://proportfolio.pro/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [blog.andreart.net](https://blog.andreart.net/?utm_source=github&utm_medium=article&utm_campaign=bio)
- [files.fm/zavadskis](https://files.fm/zavadskis?utm_source=github&utm_medium=article&utm_campaign=bio)
- [YouTube @AndrejsZavadskis](https://www.youtube.com/@AndrejsZavadskis)
- [LinkedIn](https://www.linkedin.com/in/zavadskis)
- [X @zavadskis](https://x.com/zavadskis)
- [Facebook](https://www.facebook.com/zavadskis)
