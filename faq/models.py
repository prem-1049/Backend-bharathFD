from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from googletrans import Translator

def translate_text(text, dest_lang):
    translator = Translator()
    translation = translator.translate(text, dest=dest_lang)
    return translation.text

def save_translations(instance):
    instance.question_hi = translate_text(instance.question, "hi")
    instance.question_bn = translate_text(instance.question, "bn")
    instance.answer_hi = translate_text(instance.answer, "hi")
    instance.answer_bn = translate_text(instance.answer, "bn")
    instance.save()

class FAQ(models.Model):
    question = models.TextField(_("Question"))
    answer = RichTextField(_("Answer"))
    question_hi = models.TextField(_("Question (Hindi)"), blank=True, null=True)
    question_bn = models.TextField(_("Question (Bengali)"), blank=True, null=True)
    answer_hi = RichTextField(_("Answer (Hindi)"), blank=True, null=True)
    answer_bn = RichTextField(_("Answer (Bengali)"), blank=True, null=True)

    def get_translated_question(self, lang):
        if lang == "hi":
            return self.question_hi or self.question
        elif lang == "bn":
            return self.question_bn or self.question
        return self.question

    def get_translated_answer(self, lang):
        if lang == "hi":
            return self.answer_hi or self.answer
        elif lang == "bn":
            return self.answer_bn or self.answer
        return self.answer

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        save_translations(self)

    def __str__(self):
        return self.question