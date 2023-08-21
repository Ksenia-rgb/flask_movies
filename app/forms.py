from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed, FileRequired


class ReviewForm(FlaskForm):
    name = StringField('Ваше имя', validators=[DataRequired(message='Поле не должно быть пустым'),
                                               Length(max=255, message='Введите имя длинной не более 255 символов')])
    text = TextAreaField('Текст отзыва', validators=[DataRequired(message='Поле не должно быть пустым')])
    score = SelectField('Оценка', choices=[int(i) for i in range(1, 11)])
    submit = SubmitField('Добавить отзыв')


class MovieForm(FlaskForm):
    title = StringField('Название фильма', validators=[DataRequired(message='Поле не должно быть пустым')])
    description = TextAreaField('Описание фильма', validators=[DataRequired(message='Поле не должно быть пустым')])
    image = FileField('Изображение', validators=[FileRequired(message='Поле не должно быть пустым'),
                                                 FileAllowed(['jpg', 'jpeg', 'png'], message='Неверный формат файла')])
    submit = SubmitField('Добавить фильм')



