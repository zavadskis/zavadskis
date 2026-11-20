"""Andrejs Zavadskis — bio as code. Facts only; see README.md."""

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
