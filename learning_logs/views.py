from django.shortcuts import render, redirect
from learning_logs.models import Topic, Entry
from learning_logs.forms import TopicForm, EntryForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    """Домашняя страница приложения Learning Log"""
    return render(request, 'learning_logs/index.html')


@login_required()
def topics(request):
    """Выводит список тем."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics, 'message': ''}
    return render(request, 'learning_logs/topics.html', context)


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


def topic(request, topic_id):
    """Выводит одну тему и все ее записи."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    if entries:
        context = {'topic': topic, 'entries': entries}
        return render(request, 'learning_logs/topic.html', context)
    else:
        messages.info(request, 'записей нет')
        return render(request, 'learning_logs/new_entry.html')


def new_topic(request):
    """Определяет новую тему."""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись успешно добавлена.')
            return redirect('learning_logs:topics')
    context = {'form': form}
    return render(request, "learning_logs/new_topic.html", context)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
