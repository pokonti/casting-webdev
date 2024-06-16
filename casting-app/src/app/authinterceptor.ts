import { Injectable, Provider } from '@angular/core';
import {
  HttpEvent,
  HttpInterceptor,
  HttpHandler,
  HttpRequest,
  HTTP_INTERCEPTORS,
} from '@angular/common/http';
import { Observable, tap } from 'rxjs';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
    private isLocalStorageAvailable = typeof localStorage !== 'undefined';
    constructor() {}

    intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
        if (this.isLocalStorageAvailable) {
            const access = localStorage.getItem("access")
            if (access) {
                const newRequest = request.clone({
                    headers: request.headers.set('Authorization', `Bearer ${access}`)
                });
                return next.handle(newRequest)
            }

        }
        
        console.log('Outgoing HTTP request', request);
        return next.handle(request);
    }
}

export const AuthInterceptorProvider: Provider = {
    provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true
}