self.addEventListener("install", event => {
    event.waitUntil(
        caches.open("hris-cache").then(cache => {
            return cache.addAll([
                "/",
                "/dashboard"
            ]);
        })
    );
});

self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});