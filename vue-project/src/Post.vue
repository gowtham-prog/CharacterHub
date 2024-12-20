<script>
import axios from 'axios';
import PostCard from '@/components/PostCard.vue';

export default {
    components: {
        PostCard,
    },
    data() {
        return {
            posts: [],
            loading: false,
            page: 1,
            hasMore: true,
        };
    },
    mounted() {
        this.fetchPosts();
        window.addEventListener('scroll', this.handleScroll);
    },
    beforeDestroy() {
        window.removeEventListener('scroll', this.handleScroll);
    },
    methods: {
        async fetchPosts() {
            if (this.loading || !this.hasMore) return;

            this.loading = true;

            try {
                const response = await axios.get(`http://localhost:8000/posts/?page=${this.page}`);
                const newPosts = response.data.results;

                if (newPosts.length === 0) {
                    this.hasMore = false;
                } else {
                    this.posts = [...this.posts, ...newPosts];
                    this.page++;
                }
            } catch (error) {
                console.error('Error fetching posts:', error);
            } finally {
                this.loading = false;
            }
        },
        handleScroll() {
            const bottomOfWindow =
                window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 30;

            if (bottomOfWindow && this.hasMore) {
                this.fetchPosts();
            }
        },
    },
};
</script>


<template>
    <div class="flex flex-col w-full h-full items-center p-4 ">
        <h1 class="text-3xl font-bold mb-4 text-center lg:text-4xl">Posts</h1>

        <div v-if="posts.length === 0 && !loading" class="text-center text-lg text-gray-500">
            No posts available.
        </div>

        <div v-if="posts.length > 0" class="flex flex-col flex-grow w-full h-[100vh] overflow-y-scroll">
            <PostCard v-for="post in posts" :key="post.id" :post="post" />
        </div>

        <div v-if="loading" class="text-center mt-4">
            <p class="text-lg text-gray-500">Loading more posts...</p>
        </div>
    </div>
</template>