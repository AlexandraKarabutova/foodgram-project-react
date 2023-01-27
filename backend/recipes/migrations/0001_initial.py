# Generated by Django 3.2 on 2023-01-09 19:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("tags", "0002_auto_20230105_1818"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ingredients", "0003_alter_ingredient_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="FavoriteRecipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IngredientInRecipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.PositiveIntegerField(
                        help_text="Введите количество ингридиента",
                        validators=[
                            django.core.validators.MinValueValidator(
                                1, message="Укажите количество больше либо равное 1"
                            )
                        ],
                        verbose_name="Количество ингридиента",
                    ),
                ),
                (
                    "ingredient",
                    models.ForeignKey(
                        help_text="Выберите ингредиент рецепта",
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="ingredients.ingredient",
                        verbose_name="Ингредиент рецепта",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ингредиент рецепта",
                "verbose_name_plural": "Ингредиенты рецептов",
            },
        ),
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Автоматически устанавливается текущая дата и время",
                        verbose_name="Дата создания",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите название",
                        max_length=200,
                        verbose_name="Название",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        help_text="Выберите картинку",
                        upload_to="recipes/",
                        verbose_name="Картинка",
                    ),
                ),
                (
                    "text",
                    models.TextField(
                        help_text="Введите текстовое описание",
                        verbose_name="Текстовое описание",
                    ),
                ),
                (
                    "cooking_time",
                    models.PositiveIntegerField(
                        help_text="Введите время приготовления в минутах",
                        validators=[
                            django.core.validators.MinValueValidator(
                                1, message="Укажите время больше либо равное 1"
                            )
                        ],
                        verbose_name="Время приготовления в минутах",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        help_text="Выберите из списка автора",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recipes",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
                (
                    "favorites",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Выберите пользователей, для добавления в избранное",
                        related_name="favorite_recipes",
                        through="recipes.FavoriteRecipe",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Избранное",
                    ),
                ),
                (
                    "ingredients",
                    models.ManyToManyField(
                        help_text="Выберите ингредиенты",
                        related_name="recipes",
                        through="recipes.IngredientInRecipe",
                        to="ingredients.Ingredient",
                        verbose_name="Ингредиенты",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рецепт",
                "verbose_name_plural": "Рецепты",
                "ordering": ("-created",),
                "default_related_name": "%(class)ss",
            },
        ),
        migrations.CreateModel(
            name="TagRecipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "recipe",
                    models.ForeignKey(
                        help_text="Выберите рецепт",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipes.recipe",
                        verbose_name="Рецепт",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        help_text="Выберите из списка тег",
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="tags.tag",
                        verbose_name="Тег",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ShoppingCartRecipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "recipe",
                    models.ForeignKey(
                        help_text="Выберите рецепт",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipes.recipe",
                        verbose_name="Рецепт",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="Выберите из списка автора",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="recipe",
            name="shopping_carts",
            field=models.ManyToManyField(
                blank=True,
                help_text="Выберите пользователей, для добавления в их корзины",
                related_name="shopping_cart_recipes",
                through="recipes.ShoppingCartRecipe",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Корзины",
            ),
        ),
        migrations.AddField(
            model_name="recipe",
            name="tags",
            field=models.ManyToManyField(
                help_text="Выберите теги",
                related_name="recipes",
                through="recipes.TagRecipe",
                to="tags.Tag",
                verbose_name="Теги",
            ),
        ),
        migrations.AddField(
            model_name="ingredientinrecipe",
            name="recipe",
            field=models.ForeignKey(
                help_text="Выберите рецепт",
                on_delete=django.db.models.deletion.CASCADE,
                to="recipes.recipe",
                verbose_name="Рецепт",
            ),
        ),
        migrations.AddField(
            model_name="favoriterecipe",
            name="recipe",
            field=models.ForeignKey(
                help_text="Выберите рецепт",
                on_delete=django.db.models.deletion.CASCADE,
                to="recipes.recipe",
                verbose_name="Рецепт",
            ),
        ),
        migrations.AddField(
            model_name="favoriterecipe",
            name="user",
            field=models.ForeignKey(
                help_text="Выберите из списка автора",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор",
            ),
        ),
        migrations.AddConstraint(
            model_name="tagrecipe",
            constraint=models.UniqueConstraint(
                fields=("recipe", "tag"), name="unique_recipe_tag"
            ),
        ),
        migrations.AddConstraint(
            model_name="shoppingcartrecipe",
            constraint=models.UniqueConstraint(
                fields=("recipe", "user"), name="unique_shopping_cart"
            ),
        ),
        migrations.AddConstraint(
            model_name="favoriterecipe",
            constraint=models.UniqueConstraint(
                fields=("recipe", "user"), name="unique_favorite"
            ),
        ),
    ]