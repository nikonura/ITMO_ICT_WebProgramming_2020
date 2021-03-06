# Generated by Django 3.1.2 on 2020-10-24 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presencing_publications', '0002_auto_20201025_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='a_ganre',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='career',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='death',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='direction',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='authors'),
        ),
        migrations.AlterField(
            model_name='author',
            name='second_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='b_ganre',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='books'),
        ),
        migrations.AlterField(
            model_name='book',
            name='editor',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='illustrator',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='narrator',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='trans_lang',
            field=models.CharField(blank=True, choices=[('aa', 'Afar'), ('ab', 'Abkhazian'), ('af', 'Afrikaans'), ('am', 'Amharic'), ('ar', 'Arabic'), ('as', 'Assamese'), ('ay', 'Aymara'), ('az', 'Azerbaijani'), ('ba', 'Bashkir'), ('be', 'Byelorussian'), ('bg', 'Bulgarian'), ('bh', 'Bihari'), ('bi', 'Bislama'), ('bn', 'Bengali'), ('bo', 'Tibetan'), ('br', 'Breton'), ('ca', 'Catalan'), ('co', 'Corsican'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('dz', 'Bhutani'), ('el', 'Greek'), ('en', 'English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fj', 'Fiji'), ('fo', 'Faroese'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gd', 'Scots Gaelic'), ('gl', 'Galician'), ('gn', 'Guarani'), ('gu', 'Gujarati'), ('ha', 'Hausa'), ('he', 'Hebrew'), ('iw', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hu', 'Hungarian'), ('hy', 'Armenian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('in', 'Indonesian'), ('ie', 'Interlingue'), ('ik', 'Inupiak'), ('is', 'Icelandic'), ('it', 'Italian'), ('iu', 'Inuktitut'), ('ja', 'Japanese'), ('jw', 'Javanese'), ('ka', 'Georgian'), ('kk', 'Kazakh'), ('kl', 'Greenlandic'), ('km', 'Cambodian'), ('kn', 'Kannada'), ('ko', 'Korean'), ('ks', 'Kashmiri'), ('ku', 'Kurdish'), ('ky', 'Kirghiz'), ('la', 'Latin'), ('ln', 'Lingala'), ('lo', 'Laotian'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('lv', 'Lettish'), ('mg', 'Malagasy'), ('mi', 'Maori'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mo', 'Moldavian'), ('mr', 'Marathi'), ('ms', 'Malay'), ('mt', 'Maltese'), ('my', 'Burmese'), ('na', 'Nauru'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('no', 'Norwegian'), ('oc', 'Occitan'), ('om', 'Oromo'), ('or', 'Oriya'), ('pa', 'Pundjabi'), ('pl', 'Polish'), ('ps', 'Pashto'), ('pt', 'Portuguese'), ('qu', 'Quechua'), ('rm', 'Rhaeto-Romance'), ('rn', 'Kirundi'), ('ro', 'Romanian'), ('ru', 'Russian'), ('rw', 'Kiyarwanda'), ('sa', 'Sanskrit'), ('sd', 'Sindhi'), ('sg', 'Sangho'), ('sh', 'Serbo-Croatian'), ('si', 'Singhalese'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sm', 'Samoan'), ('sn', 'Shona'), ('so', 'Somali'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('ss', 'Siswati'), ('st', 'Sesotho'), ('su', 'Sudanese'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('tg', 'Tajik'), ('th', 'Thai'), ('ti', 'Tigrinya'), ('tk', 'Turkmen'), ('tl', 'Tagalog'), ('tn', 'Setswana'), ('to', 'Tonga'), ('tr', 'Turkish'), ('ts', 'Tsonga'), ('tt', 'Tatar'), ('tw', 'Twi'), ('ug', 'Uigur'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('vi', 'Vietnamese'), ('vo', 'Volapuk'), ('wo', 'Wolof'), ('xh', 'Xhosa'), ('yi', 'Yiddish'), ('ji', 'Yiddish'), ('yo', 'Yorouba'), ('za', 'Zhuang'), ('zh', 'Chinese'), ('zu', 'Zulu')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='translator',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='type_cover',
            field=models.CharField(blank=True, choices=[('NC', 'None'), ('SC', 'Soft'), ('PB', 'Paperback'), ('OC', 'Ordinary'), ('HC', 'Hard'), ('AC', 'Audio CD'), ('AB', 'Audiobook'), ('AA', 'Audible Audio'), ('EB', 'Ebook'), ('KE', 'Kindle Edition')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='about',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='city',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='country',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='distribution',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='fact_address',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='foundation_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='founder',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='full_another_name',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='publishers'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='p_slug',
            field=models.SlugField(max_length=120, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='parent',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
